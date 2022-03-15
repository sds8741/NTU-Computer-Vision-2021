from Function import GaussianNoise, SNR
import cv2

lena = cv2.imread('lena.bmp', 0)

gauss10 = GaussianNoise(lena, 10)
gauss30 = GaussianNoise(lena, 30)

print(f'Gauss10 SNR : {SNR(lena, gauss10)}')
print(f'Gauss30 SNR : {SNR(lena, gauss30)}')
