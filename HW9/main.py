import Function
import cv2

lena = cv2.imread('lena.bmp', 0)

Robert = Function.edgeOperate(lena, 2, Function.RobertsKernel, 12)
Prewitt = Function.edgeOperate(lena, 3, Function.PrewittKernel, 24)
Sobel = Function.edgeOperate(lena, 3, Function.SobelKernel, 38)
FreiChen = Function.edgeOperate(lena, 3, Function.FreiChenKernel, 30)
Kirsch = Function.edgeOperate(lena, 3, Function.KirschKernel, 135)
Robinson = Function.edgeOperate(lena, 3, Function.RobinsonKernel, 43)
NevatiaBabu = Function.edgeOperate(lena, 5, Function.NevatiaBabuKernel, 12500)

cv2.imwrite('Robert.bmp', Robert)
cv2.imwrite('Prewitt.bmp', Prewitt)
cv2.imwrite('Sobel.bmp', Sobel)
cv2.imwrite('FreiChen.bmp', FreiChen)
cv2.imwrite('Kirsch.bmp', Kirsch)
cv2.imwrite('Robinson.bmp', Robinson)
cv2.imwrite('NevatiaBabu.bmp', NevatiaBabu)
