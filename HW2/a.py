import cv2
import matplotlib.pyplot as plt
import numpy as np
lena = cv2.imread('lena.bmp', 0)

binary = np.zeros((512, 512, 3))
for i in range(lena.shape[0]):
    for j in range(lena.shape[1]):
        if lena[i, j] >= 128:
            binary[i, j, :] = 255

plt.figure(figsize=(8, 8))
plt.imshow(binary, cmap='gray', vmin=0, vmax=255)
plt.show()
