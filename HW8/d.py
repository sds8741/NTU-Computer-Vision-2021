from Function import GaussianNoise, SaltAndPepper, MedianFilter, FilterOperate, SNR
import cv2

lena = cv2.imread('lena.bmp', 0)

gauss10 = GaussianNoise(lena, 10)
gauss30 = GaussianNoise(lena, 30)
SP5 = SaltAndPepper(lena, 0.05)
SP1 = SaltAndPepper(lena, 0.1)
Filter = MedianFilter

Median3SP5 = FilterOperate(SP5, Filter, 3)
Median3SP1 = FilterOperate(SP1, Filter, 3)
Median5SP5 = FilterOperate(SP5, Filter, 5)
Median5SP1 = FilterOperate(SP1, Filter, 5)

Median3GAU10 = FilterOperate(gauss10, Filter, 3)
Median3GAU30 = FilterOperate(gauss30, Filter, 3)
Median5SGAU10 = FilterOperate(gauss10, Filter, 5)
Median5GAU30 = FilterOperate(gauss30, Filter, 5)

print(f'Median 3x3 | S&P 0.05 SNR : {SNR(lena, Median3SP5)}')
print(f'Median 3x3 | S&P 0.1  SNR : {SNR(lena, Median3SP1)}')
print(f'Median 5x5 | S&P 0.05 SNR : {SNR(lena, Median5SP5)}')
print(f'Median 5x5 | S&P 0.1  SNR : {SNR(lena, Median5SP1)}')
print(f'Median 3x3 | Gauss10 SNR: {SNR(lena, Median3GAU10)}')
print(f'Median 3x3 | Gauss30 SNR: {SNR(lena, Median3GAU30)}')
print(f'Median 5x5 | Gauss10 SNR: {SNR(lena, Median5SGAU10)}')
print(f'Median 5x5 | Gauss30 SNR: {SNR(lena, Median5GAU30)}')
