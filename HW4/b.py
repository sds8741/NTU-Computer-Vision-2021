import matplotlib.pyplot as plt
import numpy as np
import cv2
from erosion import erosion_Octogon

lena = cv2.imread('lena.bmp', 0)
binary = np.zeros((512, 512))
for i in range(lena.shape[0]):
    for j in range(lena.shape[1]):
        if lena[i, j] >= 128:
            binary[i, j] = 1

ero_lena = binary.copy()
for i in range(binary.shape[0]):
    for j in range(binary.shape[1]):
        if binary[i, j]:
            erosion_Octogon(binary, ero_lena, [i, j])

plt.figure(figsize=(8, 8))
plt.imshow(ero_lena, cmap='gray')
plt.show()
