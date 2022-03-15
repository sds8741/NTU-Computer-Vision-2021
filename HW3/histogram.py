def histogram(img):
    hist = [0 for _ in range(256)]

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hist[img[i, j]] += 1
    return hist
