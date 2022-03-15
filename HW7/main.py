import cv2
import numpy as np
import matplotlib.pyplot as plt
from Preprocess import binary, downsample, YOKOI, pairRelationship, Thinning

lena = cv2.imread('lena.bmp', 0)

binary = binary(lena, 128)
sample = downsample(binary)
# padding = padding(sample)
# Yokoi = YOKOI(padding)
# Yokoi_padding = padding(Yokoi)
# pair = pairRelationship(Yokoi_padding)
CHAHGE = True
while CHAHGE:
    Yokoi = YOKOI(sample)
    pair = pairRelationship(Yokoi)
    thinning = Thinning(sample, pair)

    if np.array_equal(sample, thinning):
        CHAHGE = False
    else:
        sample = thinning

plt.imshow(thinning, cmap='gray')
plt.show()
