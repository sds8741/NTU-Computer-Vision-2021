
def dilation_Octogon(img, location):
    for r in range(-2, 3):
        for c in range(-2, 3):
            if abs(r) == 2 and abs(c) == 2:
                continue
            else:
                x, y = location
                if x+r < img.shape[0] and x+r >= 0 and y+c < img.shape[1] and y+c >= 0:
                    img[x+r, y+c] = 1
