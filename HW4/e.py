import matplotlib.pyplot as plt
import numpy as np
import cv2


def hit(img_original, img_ero, location):
    for r in [0, 1]:
        for c in [0, -1]:
            if r == 1 and c == -1:
                continue
            else:
                x, y = location
                if x+r < img_original.shape[0] and x+r >= 0 and y+c < img_original.shape[1] and y+c >= 0:
                    if img_original[x+r, y+c] != 1:
                        img_ero[x, y] = 0
                        return


def miss(img_original, img_ero, location):
    for r in [0, -1]:
        for c in [0, 1]:
            if r == 0 and c == 0:
                continue
            else:
                x, y = location
                if x+r < img_original.shape[0] and x+r >= 0 and y+c < img_original.shape[1] and y+c >= 0:
                    if img_original[x+r, y+c] != 1:
                        img_ero[x, y] = 0
                        return
    else:
        if not img_original[x, y]:
            img_ero[x, y] = 1


def inverse(image):
    inv_img = image.copy()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j]:
                inv_img[i, j] = 0
            else:
                inv_img[i, j] = 1
    return inv_img


def union(image1, image2):
    union_image = image1.copy()
    for i in range(image1.shape[0]):
        for j in range(image1.shape[1]):
            if image1[i, j] and image2[i, j]:
                union_image[i, j] = 1
            else:
                union_image[i, j] = 0
    return union_image


lena = cv2.imread('lena.bmp', 0)
binary = np.zeros((512, 512))
for i in range(lena.shape[0]):
    for j in range(lena.shape[1]):
        if lena[i, j] >= 128:
            binary[i, j] = 1
# Hit-Miss
inv_binary = inverse(binary)
hit_img = binary.copy()
miss_img = inv_binary.copy()

for i in range(binary.shape[0]):
    for j in range(binary.shape[1]):

        if binary[i, j]:
            hit(binary, hit_img, [i, j])

        miss(inv_binary, miss_img, [i, j])

hitmiss = union(hit_img, miss_img)

plt.figure(figsize=(8, 8))
plt.imshow(hitmiss, cmap='gray')
plt.show()
