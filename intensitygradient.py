import numpy as np
import scipy.signal as sp

def applySobelFilter(image):
    vertical = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    horizontal = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    gradient_vertical = sp.convolve2d(image, vertical, mode='same', boundary='symm')
    gradient_horizontal = sp.convolve2d(image, horizontal, mode='same', boundary='symm')

    magnitude = np.sqrt(gradient_horizontal.astype(np.float32)**2 + gradient_vertical.astype(np.float32)**2)
    
    magnitude = (magnitude / np.max(magnitude) * 255).astype(np.uint8)
    
    return gradient_vertical, gradient_horizontal, magnitude

