import numpy as np

def quantizeAngles(angles):
    quantized = np.zeros_like(angles, dtype=np.int32)
    for i in range(angles.shape[0]):
        for j in range(angles.shape[1]):
            angle = angles[i, j] % 180 
            if (angle >= 0 and angle < 22.5) or (angle >= 157.5 and angle <= 180):
                quantized[i, j] = 0
            elif angle >= 22.5 and angle < 67.5:
                quantized[i, j] = 45
            elif angle >= 67.5 and angle < 112.5:
                quantized[i, j] = 90
            elif angle >= 112.5 and angle < 157.5:
                quantized[i, j] = 135
    return quantized

def nonMaxSupression(mag, mat):
    img = np.zeros(mag.shape)
    for i in range(1, mag.shape[0] - 1):
        for j in range(1, mag.shape[1] - 1):
            angle = mat[i, j]

            if ((angle >= -22.5 and angle < 22.5) or (angle <= -157.5 and angle >= 157.5)):
                if mag[i, j] >= mag[i, j+1] and mag[i, j] >= mag[i, j-1]:
                    img[i, j] = mag[i, j]

            elif ((angle >= 22.5 and angle < 67.5) or (angle <= -112.5 and angle >= -157.5)):
                if mag[i, j] >= mag[i-1, j-1] and mag[i, j] >= mag[i+1, j+1]:
                    img[i, j] = mag[i, j]

            elif ((angle >= 67.5 and angle < 112.5) or (angle <= -67.5 and angle >= -112.5)):
                if mag[i, j] >= mag[i+1, j] and mag[i, j] >= mag[i-1, j]:
                    img[i, j] = mag[i, j]

            elif ((angle >= 112.5 and angle < 157.5) or (angle <= -22.5 and angle >= -67.5)):
                if mag[i, j] >= mag[i+1, j-1] and mag[i, j] >= mag[i-1, j+1]:
                    img[i, j] = mag[i, j]

    return img
