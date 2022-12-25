import cv2
import numpy as np

def mark(image, circles):
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(image, (x, y), r, (0, 0, 255), 4)
    return image

def movement(image, circles1, circles2):
    circles1 = np.round(circles1[0, :]).astype("int")
    circles2 = np.round(circles2[0, :]).astype("int")
    circles = zip(circles1, circles2)
    for ((x1, y1, r1), (x2, y2, r2)) in circles:
        if x1 == x2 and y1 == y2: cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 8)
        else: cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return image

def differences(img, c1, c2):
    return movement(mark(mark(img, c1), c2), c1, c2)
