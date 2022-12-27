from typing import *
import cv2 as __cv2
import numpy as __np
from . import basic as __basic


class Search:
    def __init__(self, lights: List[Tuple[int, int, int]], radius=100):
        self.pos = lights
        self.rad = radius

    @staticmethod
    def from_image(image, radius):
        circles = __basic.find(image)
        return Search(circles, radius), circles

    def update(self, image):
        cirs = []
        for i in self.pos:
            if i is None:
                cirs.append(None)
                continue
            x = int(i[0])
            y = int(i[1])
            gray = __cv2.cvtColor(image, __cv2.COLOR_BGR2GRAY)
            mask = __np.zeros(gray.shape, dtype=__np.uint8)
            w, h = self.rad, self.rad
            __cv2.circle(mask, (x, y), self.rad, 255, -1)
            masked_image = __cv2.bitwise_and(gray, gray, mask=mask)
            masked = __cv2.merge([masked_image, masked_image, masked_image])
            cir = __basic.find(masked)
            if cir is not None:
                cirs.append(cir[0])
            else:
                cirs.append(None)
        return cirs

    def use(self, updtps):
        self.pos = updtps
        return updtps

    def moves(self, updtpsp, updtps):
        c1, c2 = updtpsp, updtps
        result: List[dict] = []
        if len(c1) != len(c2):
            raise RuntimeError("Amount of circles/lights must not change!")
        circles = zip(c1, c2)
        for (a, b) in circles:
            if a is None and b is None:
                print(
                    "Invalid Entry! Circles did neither appear, disappear, change position or stay! (No data of either circle a or circle b)"
                )
            elif a is None:
                x2, y2, r2 = b
                result.append({"action": "appear", "x": int(x2), "y": int(y2), "r": int(r2)})
            elif b is None:
                x1, y1, r1 = a
                result.append({"action": "disappear", "x": int(x1), "y": int(y1), "r": int(r1)})
            else:
                x1, y1, r1 = a
                x2, y2, r2 = b
                if x1 == x2 and y1 == y2:
                    result.append({"action": "none", "x": int(x1), "y": int(y1), "r": int(r1)})
                else:
                    result.append(
                        {
                            "action": "move",
                            "from": {"x": int(x1), "y": int(y1), "r": int(r1)},
                            "to": {"x": int(x2), "y": int(y2), "r": int(r2)},
                        }
                    )
        return result, updtps
