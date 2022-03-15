import cv2
import numpy  as np
import math


def RobertsKernel(Arr):
    r1 = -Arr[0,0] + Arr[1,1]
    r2 = -Arr[0,1] + Arr[1,0]
    return math.sqrt(r1**2 + r2**2)

def PrewittKernel(Arr):
    p1 = Arr[2].sum() - Arr[0].sum()
    p2 = Arr[:,2].sum()- Arr[:,0].sum()
    return math.sqrt(p1**2 + p2**2)

def SobelKernel(Arr):
    s1 = (Arr[2,0]+2 * Arr[2,1]+Arr[2,2]) - (Arr[0,0] + 2*Arr[0,1] + Arr[0,2])
    s2 = (Arr[0,2]+2 * Arr[1,2]+Arr[2,2]) - (Arr[0,0] + 2*Arr[1,0] + Arr[2,0])
    return math.sqrt(s1**2 + s2**2)

def FreiChenKernel(Arr):
    f1 = (Arr[2,0] + math.sqrt(2) * Arr[2,1]+Arr[2,2]) - (Arr[0,0] + math.sqrt(2) * Arr[0,1] + Arr[0,2])
    f2 = (Arr[0,2] + math.sqrt(2) * Arr[1,2]+Arr[2,2]) - (Arr[0,0] + math.sqrt(2) * Arr[1,0] + Arr[2,0])
    return math.sqrt(f1**2 + f2**2)

def KirschKernel(Arr):
    kernels = np.array([
    [[-3,-3,5],[-3,0,5],[-3,-3,5]],
    [[-3,5,5],[-3,0,5],[-3,-3,-3]],
    [[5,5,5],[-3,0,-3],[-3,-3,-3]],
    [[5,5,-3],[5,0,-3],[-3,-3,-3]],
    [[5,-3,-3],[5,0,-3],[5,-3,-3]],
    [[-3,-3,-3],[5,0,-3],[5,5,-3]],
    [[-3,-3,-3],[-3,0,-3],[5,5,5]],
    [[-3,-3,-3],[-3,0,5],[-3,5,5]]])
    record = []
    for kernel in kernels:
        record.append((Arr * kernel).sum())
    return max(record)

def RobinsonKernel(Arr):
    kernels = np.array([
    [[-1,0,1],[-2,0,2],[-1,0,1]],
    [[0,1,2],[-1,0,1],[-2,-1,0]],
    [[1,2,1],[0,0,0],[-1,-2,-1]],
    [[2,1,0],[1,0,-1],[0,-1,-2]],
    [[1,0,-1],[2,0,-2],[1,0,-1]],
    [[0,-1,-2],[1,0,-1],[2,1,0]],
    [[-1,-2,-1],[0,0,0],[1,2,1]],
    [[-2,-1,0],[-1,0,1],[0,1,2]]])
    record = []
    for kernel in kernels:
        record.append((Arr * kernel).sum())
    return max(record)

def NevatiaBabuKernel(Arr):
    kernels = np.array([
    [[100,100,100,100,100],[100,100,100,100,100],[0,0,0,0,0],[-100,-100,-100,-100,-100],[-100,-100,-100,-100,-100]],
    [[100,100,100,100,100],[100,100,100,78,-32],[100,92,0,-92,-100],[32,-78,-100,-100,-100],[-100,-100,-100,-100,-100]],
    [[100,100,100,32,-100],[100,100,92,-78,-100],[100,100,0,-100,-100],[100,78,-92,-100,-100],[100,-32,-100,-100,-100]],
    [[-100,-100,0,100,100],[-100,-100,0,100,100],[-100,-100,0,100,100],[-100,-100,0,100,100],[-100,-100,0,100,100]],
    [[-100,32,100,100,100],[-100,-78,92,100,100],[-100,-100,0,100,100],[-100,-100,-92,78,100],[-100,-100,-100,-32,100]],
    [[100,100,100,100,100],[-32,78,100,100,100],[-100,-92,0,92,100],[-100,-100,-100,-78,32],[-100,-100,-100,-100,-100]],
    ])
    record = []
    for kernel in kernels:
        record.append((Arr * kernel).sum())
    return max(record)

def edgeOperate(image, kernel_size, operator, threshold):
    edge_img = image.copy()
    if kernel_size == 2:
        padding = cv2.copyMakeBorder(image,0,1,0,1,cv2.BORDER_CONSTANT,value = 0)
    else:
        s = int(kernel_size/2)
        padding = cv2.copyMakeBorder(image,s,s,s,s,cv2.BORDER_REPLICATE)
    for r in range(image.shape[0]):
        for c in range(image.shape[1]):
            arr = (padding[r:r+kernel_size,c:c+kernel_size]).astype(float)
            grad = operator(arr)
            if grad >= threshold:
                edge_img[r,c] = 0
            else:
                edge_img[r,c] = 255
    return edge_img