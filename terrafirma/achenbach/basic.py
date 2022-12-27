import cv2 as _cv2
import numpy as _np

def find(image):
    gray = _cv2.cvtColor(image, _cv2.COLOR_BGR2GRAY)
    blur = _cv2.GaussianBlur(gray, (5,5), 0)
    edges = _cv2.Canny(blur, 75, 200)
    #                                                        20         50         30            0            0 
    circles = _cv2.HoughCircles(edges, _cv2.HOUGH_GRADIENT, 1, 19, param1=10, param2=18, minRadius=0, maxRadius=0)
    if circles is not None:
        return _np.round(circles[0, :]).astype("int")
    else:
        return None
