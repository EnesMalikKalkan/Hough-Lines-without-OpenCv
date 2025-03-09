import numpy as np

def doubleThresholding(img):
    lowThresholdRatio=0.01
    highThresholdRatio=0.3
    sup = img / np.max(img)
    
    highThreshold = np.max(sup) * highThresholdRatio
    lowThreshold = highThreshold * lowThresholdRatio

    strong = (sup >= highThreshold)
    weak = ((sup < highThreshold) & (sup >= lowThreshold))
    
    return strong, weak


def hysteresis(strong, weak):
    result = np.zeros_like(strong)

    for i in range(1, strong.shape[0] - 1):
        for j in range(1, strong.shape[1] - 1):
            if strong[i, j]:
                result[i, j] = 255
            elif weak[i, j]:
                if (strong[i-1:i+2, j-1:j+2].any()): 
                    result[i, j] = 255

    return result


def doThresHyt(img):
    strong, weak = doubleThresholding(img)
    result = hysteresis(strong, weak)
    
    return result

