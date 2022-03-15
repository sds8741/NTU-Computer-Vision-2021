import cv2
import matplotlib.pyplot as plt
from histogram import histogram

lena = cv2.imread('lena.bmp', 0)
hist = histogram(lena)

plt.rcParams['axes.facecolor'] = 'black'

x = range(256)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(lena, cmap='gray')
plt.subplot(1, 2, 2)
plt.bar(x, hist, width=1, color='white')
plt.xlabel('Gray level')
plt.ylabel('Pixels number')
plt.show()
