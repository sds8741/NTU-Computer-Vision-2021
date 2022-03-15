from Function import SaltAndPepper, SNR
import cv2

lena = cv2.imread('lena.bmp', 0)

SPoo5 = SaltAndPepper(lena, 0.05)
SPo1 = SaltAndPepper(lena, 0.1)

print(f'S&P 0.05 SNR : {SNR(lena, SPoo5)}')
print(f'S&P 0.1  SNR : {SNR(lena, SPo1)}')
