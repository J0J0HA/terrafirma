from typing import *
import cv2
import numpy as np
from . import basic

class ImageSearcher:
    def __init__(self, lights: List[Tuple[int, int, int]], radius=100):
        self.pos = lights
        self.rad = radius
    
    def update(self, image):
        cirs = []
        for i in self.pos:
            x = int(i[0])
            y = int(i[1])
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            mask = np.zeros(gray.shape, dtype=np.uint8)
            w, h = self.rad, self.rad
            cv2.circle(mask, (x, y), self.rad, 255, -1)
            masked_image = cv2.bitwise_and(gray, gray, mask=mask)
            masked = cv2.merge([masked_image, masked_image, masked_image])
            cir = basic.find(masked)
            if cir is not None:
                cirs.append(cir[0])
            else:
                cirs.append(None)
        return cirs
    
    def use(self, updtps):
        self.pos = updtps
        return updtps
