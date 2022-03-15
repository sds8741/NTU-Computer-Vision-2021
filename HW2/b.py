import cv2
import matplotlib.pyplot as plt

lena = cv2.imread('lena.bmp', 0)
hist = [0 for x in range(256)]

for i in range(lena.shape[0]):
    for j in range(lena.shape[1]):
        hist[lena[i, j]] += 1

plt.rcParams['axes.facecolor'] = 'black'

x = range(256)
plt.bar(x, hist, width=1, color='white')

plt.xlabel('Gray level')
plt.ylabel('Pixels number')
plt.show()


