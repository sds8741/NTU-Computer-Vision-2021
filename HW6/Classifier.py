import numpy as np

# Classify a pixel by YOKOI connectivity number


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
