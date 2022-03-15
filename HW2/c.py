import cv2
import matplotlib.pyplot as plt
import numpy as np

lena = cv2.imread('lena.bmp', 0)
# read the image from b result
binary = cv2.imread('./HW2/binaryimage.bmp')
label = np.zeros(lena.shape)
record = 1
# Label each nonzero pixel to unique label
for i in range(lena.shape[0]):
    for j in range(lena.shape[1]):
        if binary[i, j, 0] != 0:
            label[i, j] = record
            record += 1

CHANGE = True
# finish iterative algorithm if it didn't change
while CHANGE:
    CHANGE = False
    # top-down pass
    for i in range(lena.shape[0]-1):
        for j in range(lena.shape[1]-1):
            if label[i, j] != 0:
                if label[i+1, j] > label[i, j]:
                    label[i+1, j] = label[i, j]
                    CHANGE = True
                if label[i, j+1] > label[i, j]:
                    label[i, j+1] = label[i, j]
                    CHANGE = True
    # bottom-up pass
    for i in range(lena.shape[0]-1, 0, -1):
        for j in range(lena.shape[1]-1, 0, -1):
            if label[i, j] != 0:
                if label[i-1, j] > label[i, j]:
                    label[i-1, j] = label[i, j]
                    CHANGE = True
                if label[i, j-1] > label[i, j]:
                    label[i, j-1] = label[i, j]
                    CHANGE = True

label = label.astype(int)
# record label number
pixel_label = dict.fromkeys(range(1, label.max()+1), 0)
for i in range(lena.shape[0]):
    for j in range(lena.shape[1]):
        if label[i, j] != 0:
            pixel_label[label[i, j]] += 1
final_label = []
# record the label when pixel > 500
for key in pixel_label:
    if pixel_label[key] > 500:
        final_label.append(key)

for num in final_label:
    xloc, yloc = [], []
    for y in range(lena.shape[0]):
        for x in range(lena.shape[1]):
            if label[y, x] == num:
                xloc.append(x)
                yloc.append(y)

    cv2.rectangle(binary, (min(xloc), min(yloc)),
                  (max(xloc), max(yloc)), (0, 0, 255), 4)
    # calculate the centroid
    sign_row, sign_col = {}, {}
    for row in list(set(xloc)):
        count = 0
        for pixel in xloc:
            if pixel == row:
                count += 1
        sign_row[row] = count
    for col in list(set(yloc)):
        count = 0
        for pixel in yloc:
            if pixel == col:
                count += 1
        sign_col[col] = count

    centroidy = int(sum([sign_col[r]*r for r in sign_col])/len(xloc))
    centroidx = int(sum([sign_row[r]*r for r in sign_row])/len(yloc))

    cv2.circle(binary, (centroidx, centroidy), 3, (255, 0, 0), 4)

plt.figure(figsize=(8, 8))
plt.imshow(binary, cmap='gray', vmin=0, vmax=255)
plt.show()
