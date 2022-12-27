import cv2 as _cv2
import numpy as _np

def mark(image, circles):
    img = image.copy()
    if circles is not None:
        for i in circles:
            if i is None:
                print("Invalid Entry! No data given!")
                continue
            else:
                x, y, r = int(i[0]), int(i[1]), int(i[2])
            _cv2.circle(img, (x, y), r, (0, 0, 255), 4)
    return img

def movement(shape, circles1, circles2):
    image = _np.zeros(shape, dtype=_np.uint8)
    return movement_image(image, circles1, circles2)

def movement_image(image, circles1, circles2):
    img = image.copy()
    if len(circles1) != len(circles2):
        raise RuntimeError("Amount of circles/lights must not change!")
    circles = zip(circles1, circles2)
    for (a, b) in circles:
        if a is None and b is None:
            print("Invalid Entry! Circles did neither appear, disappear, change position or stay! (No data of either circle a or circle b)")
        elif a is None:
            x2, y2, r2 = b
            _cv2.circle(img, (x2, y2), r2, (0, 0, 255), 4)
        elif b is None:
            x1, y1, r1 = a
            _cv2.circle(img, (x1, y1), r1, (0, 0, 255), 4)
        else:
            x1, y1, r1 = a
            x2, y2, r2 = b
            if x1 == x2 and y1 == y2:
                _cv2.circle(img, (x1, y1), r1, (0, 255, 0), 2)
            else:
                _cv2.circle(img, (x1, y1), r1, (0, 50, 255), 2)
                _cv2.circle(img, (x2, y2), r2, (255, 50, 50), 3)
                _cv2.arrowedLine(img, (x1, y1), (x2, y2), (0, 255, 255), 1)
    return img
