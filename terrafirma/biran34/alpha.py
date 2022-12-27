import cv2
import numpy as np

def visualize(shape, moves):
    img = np.zeros(shape, dtype=np.uint8)
    for move in moves:
        match move["action"]:
            case "appear":
                cv2.circle(img, (move["x"], move["y"]), move["r"], (0, 0, 255), 4)
            case "disappear":
                cv2.circle(img, (move["x"], move["y"]), move["r"], (0, 0, 255), 4)
            case "move":
                cv2.circle(img, (move["from"]["x"], move["from"]["y"]), move["from"]["r"], (0, 50, 255), 2)
                cv2.circle(img, (move["to"]["x"], move["to"]["y"]), move["to"]["r"], (255, 50, 50), 3)
                cv2.arrowedLine(img, (move["from"]["x"], move["from"]["y"]), (move["to"]["x"], move["to"]["y"]), (0, 255, 255), 1)
            case "none":
                cv2.circle(img, (move["x"], move["y"]), move["r"], (0, 255, 0), 2)
    return img

def visualize_on_img(image, moves):
    img = image.copy()
    for move in moves:
        match move["action"]:
            case "appear":
                cv2.circle(img, (move["x"], move["y"]), move["r"], (0, 0, 255), 4)
            case "disappear":
                cv2.circle(img, (move["x"], move["y"]), move["r"], (0, 0, 255), 4)
            case "move":
                cv2.circle(img, (move["from"]["x"], move["from"]["y"]), move["from"]["r"], (0, 50, 255), 2)
                cv2.circle(img, (move["to"]["x"], move["to"]["y"]), move["to"]["r"], (255, 50, 50), 3)
                cv2.arrowedLine(img, (move["from"]["x"], move["from"]["y"]), (move["to"]["x"], move["to"]["y"]), (0, 255, 255), 1)
            case "none":
                cv2.circle(img, (move["x"], move["y"]), move["r"], (0, 255, 0), 2)
    return img