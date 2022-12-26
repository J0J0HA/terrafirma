import cv2
import numpy as np

def find(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 75, 200)
    #                                                        20         50         30            0            0 
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param1=10, param2=18, minRadius=0, maxRadius=0)
    if circles is not None:
        return np.round(circles[0, :]).astype("int")
    else:
        return None
