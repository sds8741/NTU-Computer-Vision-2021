import cv2
import numpy as np
from Classifier import classifier

lena = cv2.imread('lena.bmp', 0)

# binarize the image
binary = np.zeros((512, 512))
for i in range(lena.shape[0]):
    for j in range(lena.shape[1]):
        if lena[i, j] >= 128:
            binary[i, j] = 255

# down-sample lena with 8*8 block
sample = []
for i in range(0, lena.shape[0], 8):
    for j in range(0, lena.shape[1], 8):
        sample.append(binary[i, j])
sample = np.array(sample)
lena_down = sample.reshape(64, 64)

# padding the lena image
padding = np.zeros([66, 66])
for i in range(lena_down.shape[0]):
    for j in range(lena_down.shape[1]):
        padding[i+1, j+1] = lena_down[i, j]

YOKOI = np.zeros((64, 64))
for i in range(YOKOI.shape[0]):
    for j in range(YOKOI.shape[1]):
        if padding[i+1, j+1]:
            YOKOI[i, j] = classifier(padding, [i+1, j+1])

# Write the YOKOI result to a txt file
path = 'output.txt'
with open(path, 'w') as f:
    for i in range(len(YOKOI)):
        string = [str(int(s)) for s in YOKOI[i]]
        for c in string:
            f.write(c)
        f.write('\n')
