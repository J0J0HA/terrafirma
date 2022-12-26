import cv2
import numpy as np

def mark(image, circles):
    img = image.copy()
    if circles is not None:
        for i in circles:
            if i is None:
                continue
            else:
                x, y, r = int(i[0]), int(i[1]), int(i[2])
            cv2.circle(img, (x, y), r, (0, 0, 255), 4)
    return img

def movement(image, circles1, circles2):
    img = image.copy()
    if len(circles1) != len(circles2):
        raise RuntimeError("Amount of circles/lights must not change!")
    circles = zip(circles1, circles2)
    for (a, b) in circles:
        x1, y1, r1 = a
        if b is None:
            cv2.circle(img, (x1, y1), r1, (0, 255, 255), 4)
        else:
            x2, y2, r2 = b
            if x1 == x2 and y1 == y2:
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 8)
                cv2.circle(img, (x1, y1), r1, (0, 0, 255), 4)
            else:
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(img, (x2, y2), r2, (0, 0, 255), 4)
    return img

def differences(image, c1, c2):
    img = image.copy()
    img = mark(img, c1)
    img = mark(img, c2)
    img = movement(img, c1, c2)
    return img
