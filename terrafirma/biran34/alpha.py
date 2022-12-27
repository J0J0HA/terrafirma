import cv2 as __cv2
import numpy as __np

def visualize(shape, moves):
    image = __np.zeros(shape, dtype=__np.uint8)
    return visualize_image(image, moves)

def visualize_image(image, moves):
    img = image.copy()
    for move in moves:
        match move["action"]:
            case "appear":
                __cv2.circle(img, (move["x"], move["y"]), move["r"], (0, 0, 255), 4)
            case "disappear":
                __cv2.circle(img, (move["x"], move["y"]), move["r"], (0, 0, 255), 4)
            case "move":
                __cv2.circle(img, (move["from"]["x"], move["from"]["y"]), move["from"]["r"], (0, 50, 255), 2)
                __cv2.circle(img, (move["to"]["x"], move["to"]["y"]), move["to"]["r"], (255, 50, 50), 3)
                __cv2.arrowedLine(img, (move["from"]["x"], move["from"]["y"]), (move["to"]["x"], move["to"]["y"]), (0, 255, 255), 1)
            case "none":
                __cv2.circle(img, (move["x"], move["y"]), move["r"], (0, 255, 0), 2)
    return img