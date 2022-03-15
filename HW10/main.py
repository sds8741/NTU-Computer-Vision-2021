import cv2
import numpy as np


def Laplacian(image, kernel_size, kernel, threshold):  # output 1,-1 or 0
    Laplacian_img = image.copy().astype(float)
    s = int(kernel_size/2)
    padding = cv2.copyMakeBorder(image, s, s, s, s, cv2.BORDER_REPLICATE)
    for r in range(image.shape[0]):
        for c in range(image.shape[1]):
            arr = (padding[r:r+kernel_size, c:c+kernel_size]).astype(float)
            grad = (arr * kernel).sum()
            if grad >= threshold:
                Laplacian_img[r, c] = 1
            elif grad <= -1 * threshold:
                Laplacian_img[r, c] = -1
            else:
                Laplacian_img[r, c] = 0
    return Laplacian_img


def zeroCrossing(image):  # output edge image
    edge_img = image.copy()
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    padding = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_REPLICATE)
    for r in range(image.shape[0]):
        for c in range(image.shape[1]):
            if image[r, c] > 0 and (padding[r:r+3, c:c+3]*kernel < 0).any():
                edge_img[r, c] = 0
            else:
                edge_img[r, c] = 255
    return edge_img


# Masks
# (a)
K1 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
# (b)
K2 = (1/3) * np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
# (c)
K3 = (1/3) * np.array([[2, -1, 2], [-1, -4, -1], [2, -1, 2]])
# (d)
K4 = np.array([[0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0],
               [0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0],
               [0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0],
               [-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1],
               [-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1],
               [-2, -9, -23, -1, 103, 178, 103, -1, -23, -9, -2],
               [-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1],
               [-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1],
               [0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0],
               [0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0],
               [0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0]])
# (e)
K5 = np.array([[-1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1],
               [-3, -5, -8, -11, -13, -13, -13, -11, -8, -5, -3],
               [-4, -8, -12, -16, -17, -17, -17, -16, -12, -8, -4],
               [-6, -11, -16, -16, 0, 15, 0, -16, -16, -11, -6],
               [-7, -13, -17, 0, 85, 160, 85, 0, -17, -13, 17],
               [-8, -13, -17, 15, 160, 283, 160, 15, -17, -13, -8],
               [-7, -13, -17, 0, 85, 160, 85, 0, -17, -13, 17],
               [-6, -11, -16, -16, 0, 15, 0, -16, -16, -11, -6],
               [-4, -8, -12, -16, -17, -17, -17, -16, -12, -8, -4],
               [-3, -5, -8, -11, -13, -13, -13, -11, -8, -5, -3],
               [-1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1]])

masks = [K1, K2, K3, K4, K5]
thresholds = [15, 15, 20, 3000, 1]
lena = cv2.imread('lena.bmp', 0)
for i, (mask, t) in enumerate(zip(masks, thresholds)):
    L = Laplacian(lena, len(mask), mask, t)
    output = zeroCrossing(L)
    cv2.imwrite(f'{i}.bmp', output)
