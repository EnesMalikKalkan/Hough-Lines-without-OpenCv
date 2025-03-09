import numpy as np

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = np.round(0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)

    return gray
