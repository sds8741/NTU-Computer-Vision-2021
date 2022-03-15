from Function import GaussianNoise, SaltAndPepper, SNR, opening_closing, closing_opening
import cv2
import numpy as np

lena = cv2.imread('lena.bmp', 0)

kernel = np.array([[0, 0], [1, 0], [2, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 1],
                   [-1, 0], [-2, 0], [-1, 1], [-1, 2], [-2, 1],
                   [0, -1], [0, -2], [1, -1], [1, -2], [2, -1],
                   [-1, -1], [-1, -2], [-2, -1],
                   ])

gauss10 = GaussianNoise(lena, 10)
gauss30 = GaussianNoise(lena, 30)
SP5 = SaltAndPepper(lena, 0.05)
SP1 = SaltAndPepper(lena, 0.1)

OCGAU10 = opening_closing(gauss10, kernel)
OCGAU30 = opening_closing(gauss30, kernel)
OCSP5 = opening_closing(SP5, kernel)
OCSP1 = opening_closing(SP1, kernel)

COGAU10 = closing_opening(gauss10, kernel)
COGAU30 = closing_opening(gauss30, kernel)
COSP5 = closing_opening(SP5, kernel)
COSP1 = closing_opening(SP1, kernel)

print(f'Opening-then-closing | S&P 0.05 SNR : {SNR(lena, OCSP5)}')
print(f'Opening-then-closing | S&P 0.1  SNR : {SNR(lena, OCSP1)}')
print(f'Closing-then-opening | S&P 0.05 SNR : {SNR(lena, COSP5)}')
print(f'Closing-then-opening | S&P 0.1  SNR : {SNR(lena, COSP1)}')
print(f'Opening-then-closing | Gauss10 SNR: {SNR(lena, OCGAU10)}')
print(f'Opening-then-closing | Gauss30 SNR: {SNR(lena, OCGAU30)}')
print(f'Closing-then-opening | Gauss10 SNR: {SNR(lena, COGAU10)}')
print(f'Closing-then-opening | Gauss30 SNR: {SNR(lena, COGAU30)}')
