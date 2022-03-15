import cv2
import numpy as np
import random


def GaussianNoise(original_image, amplitude):
    Gaussian_image = original_image.copy()
    for c in range(original_image.shape[0]):
        for r in range(original_image.shape[1]):
            noisePixel = int(
                original_image[c, r] + amplitude * random.gauss(0, 1))
            if noisePixel > 255:
                noisePixel = 255
            Gaussian_image[c, r] = noisePixel
    return Gaussian_image


def SaltAndPepper(original_image, threshold):
    SaltAndPepper_image = original_image.copy()
    for c in range(original_image.shape[0]):
        for r in range(original_image.shape[1]):
            rand = random.uniform(0, 1)
            if rand <= threshold:
                SaltAndPepper_image[c, r] = 0
            elif rand >= 1 - threshold:
                SaltAndPepper_image[c, r] = 255
    return SaltAndPepper_image


def BoxFilter(arr, size):
    boxArr = (1/size**2) * np.ones([size, size])
    return round(np.sum(arr * boxArr))


def MedianFilter(arr, size):
    return round(np.median(arr))


def FilterOperate(Image, FilterFunction, size):
    padding_size = int((size-1)/2)
    padding = cv2.copyMakeBorder(
        Image, padding_size, padding_size, padding_size, padding_size, cv2.BORDER_REFLECT)
    filter_image = Image.copy()
    for r in range(Image.shape[0]):
        for c in range(Image.shape[1]):
            Array = padding[r:r+size, c:c+size]
            pixel = FilterFunction(Array, size)
            filter_image[r, c] = pixel
    return filter_image


def dilation(img, kernel):
    dil_img = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            record = []
            coord = [i, j]
            for move in kernel:
                try:
                    record.append(img[tuple(coord + move)])
                except:
                    continue
            dil_img[tuple(coord)] = max(record)
    return dil_img


def erosion(img, kernel):
    ero_img = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            record = []
            coord = [i, j]
            for move in kernel:
                try:
                    record.append(img[tuple(coord + move)])
                except:
                    continue
            ero_img[tuple(coord)] = min(record)
    return ero_img


def opening(img, kernel):
    opening_img = erosion(img, kernel)
    opening_img = dilation(opening_img, kernel)
    return opening_img


def closing(img, kernel):
    closing_img = dilation(img, kernel)
    closing_img = erosion(closing_img, kernel)
    return closing_img


def opening_closing(img, kernel):
    open = opening(img, kernel)
    close = closing(open, kernel)
    return close


def closing_opening(img, kernel):
    close = closing(img, kernel)
    open = opening(close, kernel)
    return open


def SNR(original, noise_image):

    original_nor = original/255.
    noise_image_nor = noise_image/255.

    noise = noise_image_nor - original_nor

    return 20 * np.log10((original_nor.std() / noise.std()))
