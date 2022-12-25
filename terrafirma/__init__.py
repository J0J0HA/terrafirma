from . import achenbach, biran34
import cv2 as __


img = __.imread
def show(title, img):
    __.imshow(title, img)
    __.waitKey(0)