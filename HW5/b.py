import numpy as np
import matplotlib.pyplot as plt
import cv2

from erosion import erosion

lena = cv2.imread('lena.bmp', 0)

kernel = np.array([[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 3], [1, 3],
                   [-1, 0], [-2, 0], [-1, 1], [-2, 1], [-1, 3],
                   [0, -1], [0, -2], [1, -1], [2, -1], [1, -2], [-1, -1], [-2, -1], [-1, -3]])

ero_lena = erosion(lena, kernel)

plt.figure(figsize=(8, 8))
plt.imshow(ero_lena, cmap='gray', vmin=0, vmax=255)
plt.show()
