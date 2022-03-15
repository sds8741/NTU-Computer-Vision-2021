import matplotlib.pyplot as plt
import numpy as np
import cv2
from erosion import erosion_Octogon
from dilation import dilation_Octogon

lena = cv2.imread('lena.bmp', 0)
binary = np.zeros((512, 512))
for i in range(lena.shape[0]):
    for j in range(lena.shape[1]):
        if lena[i, j] >= 128:
            binary[i, j] = 1

# Closing
closing_lena = binary.copy()
# dilation
for i in range(binary.shape[0]):
    for j in range(binary.shape[1]):
        if binary[i, j]:
            dilation_Octogon(closing_lena, [i, j])
# erosion
copy_lena = closing_lena.copy()
for i in range(binary.shape[0]):
    for j in range(binary.shape[1]):
        if copy_lena[i, j]:
            erosion_Octogon(copy_lena, closing_lena, [i, j])

plt.figure(figsize=(8, 8))
plt.imshow(closing_lena, cmap='gray')
plt.show()
