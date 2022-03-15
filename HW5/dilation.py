import numpy as np


def dilation(img, kernel):
    dil_img = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            record = []
            coord = [i, j]
            for move in kernel:
                try:
                    record.append(img[tuple(coord + move)])
                except:
                    continue
            dil_img[tuple(coord)] = max(record)
    return dil_img
