import cv2
import numpy as np
import matplotlib.pyplot as plt
from grayimg import rgb2gray # Convert image to grayscale
from blurimg import applyGaussianFilter # Image blurring
from intensitygradient import applySobelFilter # Applying sobel filter for edge detection and normalizing the results
from nms import nonMaxSupression # Used to identify the strongest edges
from dth import doThresHyt # Used to ensure edge continuity
from hough import hough # Hough transform and plotting the found edges

num_rho = 180
num_theta = 180
threshold = 300

image = cv2.imread("path of the image's")
grayimg = rgb2gray(image)
blurimg = applyGaussianFilter(grayimg)
x, y, mag = applySobelFilter(blurimg)
mat = np.degrees(np.arctan2(y, x))
nms = nonMaxSupression(mag, mat)
dth = doThresHyt(nms)

plt.imshow(dth, cmap="gray")
plt.title("Detected Edges")
plt.axis("off")
plt.show()

line_image, lines = hough(image, dth, num_rho, num_theta, threshold)
plt.imshow(line_image, cmap="gray")
plt.title("Detected Lines")
plt.axis("off")
plt.show()



