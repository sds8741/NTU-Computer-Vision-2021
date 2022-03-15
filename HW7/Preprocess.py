import numpy as np


def binary(img, threshold):

    binary = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] >= threshold:
                binary[i, j] = 255
    return binary


def downsample(img):
    sample = []
    size = int(img.shape[0] / 8)
    for i in range(0, img.shape[0], 8):
        for j in range(0, img.shape[1], 8):
            sample.append(img[i, j])
    sample = np.array(sample)
    reshape_sample = sample.reshape(size, size)
    return reshape_sample


def padding(img):
    w, h = img.shape
    padding = np.zeros([w+2, h+2])
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            padding[i+1, j+1] = img[i, j]
    return padding


def classifier(image, point):  # point : the pixel location

    # store every corner Neighborhood
    refere = {
        'a1': np.array([[1, 0], [1, 1], [0, 1]]),
        'a2': np.array([[0, 1], [-1, 1], [-1, 0]]),
        'a3': np.array([[-1, 0], [-1, -1], [0, -1]]),
        'a4': np.array([[0, -1], [1, -1], [1, 0]]),
    }
    # record q, r number
    record = dict.fromkeys(['r', 'q'], 0)

    for key in refere:
        for n, ele in enumerate(refere[key]):
            # the first neighbor is not a objective (s class)
            if n == 0 and not image[tuple(point + ele)]:
                break
            elif not image[tuple(point + ele)]:
                record['q'] += 1
                break
        else:
            record['r'] += 1

    if record['r'] == 4:
        return 5
    else:
        return record['q']


def YOKOI(img):
    img_padding = padding(img)
    w, h = img_padding.shape
    YOKOI = np.zeros((w-2, h-2))
    for i in range(YOKOI.shape[0]):
        for j in range(YOKOI.shape[1]):
            if img_padding[i+1, j+1]:
                YOKOI[i, j] = classifier(img_padding, [i+1, j+1])
    return YOKOI


def pairRelationship(YOKOI):
    fourconnect = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])
    YOKOI_padding = padding(YOKOI)
    w, h = YOKOI_padding.shape
    output = np.full((w-2, h-2), 'q')
    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            loc = [i+1, j+1]
            if YOKOI_padding[tuple(loc)] == 1:
                for move in fourconnect:
                    if YOKOI_padding[tuple(loc + move)] == 1:
                        output[i, j] = 'p'
                        break
    return output


def Thinning(original, pair):
    original_padding = padding(original)
    for i in range(original.shape[0]):
        for j in range(original.shape[1]):
            if pair[i, j] == 'p':
                number = classifier(original_padding, [i+1, j+1])
                if number == 1:
                    original_padding[i+1, j+1] = 0
    return original_padding[1:-1, 1:-1]
