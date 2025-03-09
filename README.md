# HoughLines-without-OpenCV
**main.py:** file is the one where the operations of the project are performed.

**grayimg.py:** file converts the loaded image into grayscale.

**blurimg.py:** file performs the blurring operation on the grayscale image using a Gaussian filter.

**intensitygradient.py:** file detects edges within the grayscale and blurred image by applying the Sobel filter and normalizes the result.

**nms.py:** file, edges detected below a given threshold are suppressed, while edges above the threshold are enhanced, making the edges more prominent.

**dth.py:** file attempts to connect disconnected points to form an edge.

**hough.py:** file, the Hough transform is applied, and the edges found in the original image are drawn.
