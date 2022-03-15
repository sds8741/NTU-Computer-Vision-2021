from Function import GaussianNoise, SaltAndPepper, BoxFilter, FilterOperate, SNR
import cv2

lena = cv2.imread('lena.bmp', 0)

gauss10 = GaussianNoise(lena, 10)
gauss30 = GaussianNoise(lena, 30)
SP5 = SaltAndPepper(lena, 0.05)
SP1 = SaltAndPepper(lena, 0.1)
Filter = BoxFilter

box3SP5 = FilterOperate(SP5, Filter, 3)
box3SP1 = FilterOperate(SP1, Filter, 3)
box5SP5 = FilterOperate(SP5, Filter, 5)
box5SP1 = FilterOperate(SP1, Filter, 5)

box3GAU10 = FilterOperate(gauss10, Filter, 3)
box3GAU30 = FilterOperate(gauss30, Filter, 3)
box5SGAU10 = FilterOperate(gauss10, Filter, 5)
box5GAU30 = FilterOperate(gauss30, Filter, 5)

print(f'Box 3x3 | S&P 0.05 SNR : {SNR(lena, box3SP5)}')
print(f'Box 3x3 | S&P 0.1  SNR : {SNR(lena, box3SP1)}')
print(f'Box 5x5 | S&P 0.05 SNR : {SNR(lena, box5SP5)}')
print(f'Box 5x5 | S&P 0.1  SNR : {SNR(lena, box5SP1)}')
print(f'Box 3x3 | Gauss10 SNR: {SNR(lena, box3GAU10)}')
print(f'Box 3x3 | Gauss30 SNR: {SNR(lena, box3GAU30)}')
print(f'Box 5x5 | Gauss10 SNR: {SNR(lena, box5SGAU10)}')
print(f'Box 5x5 | Gauss30 SNR: {SNR(lena, box5GAU30)}')
