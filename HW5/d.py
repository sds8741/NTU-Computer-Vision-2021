import numpy as np
import matplotlib.pyplot as plt
import cv2

from dilation import dilation
from erosion import erosion


def closing(img, kernel):
    closing_img = dilation(img, kernel)
    closing_img = erosion(closing_img, kernel)
    return closing_img


lena = cv2.imread('lena.bmp', 0)

kernel = np.array([[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 3], [1, 3],
                   [-1, 0], [-2, 0], [-1, 1], [-2, 1], [-1, 3],
                   [0, -1], [0, -2], [1, -1], [2, -1], [1, -2], [-1, -1], [-2, -1], [-1, -3]])

opening_lena = closing(lena, kernel)

plt.figure(figsize=(8, 8))
plt.imshow(opening_lena, cmap='gray', vmin=0, vmax=255)
plt.show()
