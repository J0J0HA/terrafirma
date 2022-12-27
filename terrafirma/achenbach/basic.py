import cv2 as __cv2
import numpy as __np

def find(image):
    gray = __cv2.cvtColor(image, __cv2.COLOR_BGR2GRAY)
    blur = __cv2.GaussianBlur(gray, (5,5), 0)
    edges = __cv2.Canny(blur, 75, 200)
    #                                                        20         50         30            0            0 
    circles = __cv2.HoughCircles(edges, __cv2.HOUGH_GRADIENT, 1, 19, param1=10, param2=18, minRadius=0, maxRadius=0)
    if circles is not None:
        return __np.round(circles[0, :]).astype("int")
    else:
        return None
