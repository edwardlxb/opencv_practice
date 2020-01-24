import cv2
import numpy
image = cv2.imread("/Users/xinbolu/Downloads/logo.png")

cv2.imshow("OpenCV logo", image)

cv2.waitKey(0)

cv2.destroyAllWindows()