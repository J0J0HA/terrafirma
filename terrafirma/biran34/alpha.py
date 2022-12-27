import cv2 as _cv2
import numpy as _np

def visualize(shape, moves):
    image = _np.zeros(shape, dtype=_np.uint8)
    return visualize_image(image, moves)

def visualize_image(image, moves):
    img = image.copy()
    for move in moves:
        match move["action"]:
            case "appear":
                _cv2.circle(img, (move["x"], move["y"]), move["r"], (0, 0, 255), 4)
            case "disappear":
                _cv2.circle(img, (move["x"], move["y"]), move["r"], (0, 0, 255), 4)
            case "move":
                _cv2.circle(img, (move["from"]["x"], move["from"]["y"]), move["from"]["r"], (0, 50, 255), 2)
                _cv2.circle(img, (move["to"]["x"], move["to"]["y"]), move["to"]["r"], (255, 50, 50), 3)
                _cv2.arrowedLine(img, (move["from"]["x"], move["from"]["y"]), (move["to"]["x"], move["to"]["y"]), (0, 255, 255), 1)
            case "none":
                _cv2.circle(img, (move["x"], move["y"]), move["r"], (0, 255, 0), 2)
    return img