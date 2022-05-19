import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    _, img = cap.read()
    cv2.imshow("Output",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows(0)