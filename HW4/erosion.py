def erosion_Octogon(img_original, img_ero, location):
    for r in range(-2, 3):
        for c in range(-2, 3):
            if abs(r) == 2 and abs(c) == 2:
                continue
            else:
                x, y = location
                if x+r < img_original.shape[0] and x+r >= 0 and y+c < img_original.shape[1] and y+c >= 0:
                    if not img_original[x+r, y+c]:
                        img_ero[x, y] = 0
                        return
