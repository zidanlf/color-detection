import numpy as np
import cv2

def get_limits(color, name=None):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    h = hsvC[0][0][0]

    if name == "red":
        lowerLimit = np.array([0, 150, 120], dtype=np.uint8)
        upperLimit = np.array([2, 255, 255], dtype=np.uint8)
        return (lowerLimit, upperLimit)

    elif name == "yellow":
        lowerLimit = np.array([h - 10, 120, 120], dtype=np.uint8)
        upperLimit = np.array([h + 10, 255, 255], dtype=np.uint8)
        return (lowerLimit, upperLimit)

    elif name == "blue":
        lowerLimit = np.array([h - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([h + 10, 255, 255], dtype=np.uint8)
        return (lowerLimit, upperLimit)