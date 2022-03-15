import numpy as np


def erosion(img, kernel):
    ero_img = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            record = []
            coord = [i, j]
            for move in kernel:
                try:
                    record.append(img[tuple(coord + move)])
                except:
                    continue
            ero_img[tuple(coord)] = min(record)
    return ero_img
