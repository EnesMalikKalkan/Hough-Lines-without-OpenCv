import numpy as np

def gaussianKernel():
    sigma = 1.0
    size = 5
    kernel = np.zeros((size, size))
    center = size // 2
    for x in range(size):
        for y in range(size):
            diff = (x - center)**2 + (y - center)**2
            kernel[x, y] = (1/(2 * np.pi * sigma**2)) * (np.exp(-diff / (2 * sigma**2)))
    kernel /= np.sum(kernel)
    return kernel

def applyGaussianFilter(image):
    kernel = gaussianKernel() 
    h, w = image.shape
    kh, kw = 5, 5
    pad_h, pad_w = kh // 2, kw // 2

    padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
    filtered_image = np.zeros_like(image) 

    for i in range(h):
        for j in range(w):
            region = padded_image[i:i + kh, j:j + kw]
            filtered_image[i, j] = np.sum(region * kernel)
            
    return filtered_image.astype(np.uint8)

