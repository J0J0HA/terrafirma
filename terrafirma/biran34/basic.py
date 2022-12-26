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
    img = np.zeros(image.shape, dtype=np.uint8)
    if len(circles1) != len(circles2):
        raise RuntimeError("Amount of circles/lights must not change!")
    circles = zip(circles1, circles2)
    for (a, b) in circles:
        if a is None and b is None:
            print("Invalid Entry")
        elif a is None:
            x2, y2, r2 = b
            cv2.circle(img, (x2, y2), r2, (0, 0, 255), 4)
        elif b is None:
            x1, y1, r1 = a
            cv2.circle(img, (x1, y1), r1, (0, 0, 255), 4)
        else:
            x1, y1, r1 = a
            x2, y2, r2 = b
            if x1 == x2 and y1 == y2:
                cv2.circle(img, (x1, y1), r1, (0, 255, 0), 2)
            else:
                cv2.circle(img, (x1, y1), r1, (0, 50, 255), 2)
                cv2.circle(img, (x2, y2), r2, (255, 50, 50), 3)
                cv2.arrowedLine(img, (x1, y1), (x2, y2), (0, 255, 255), 1)
    return img
