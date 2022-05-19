import cv2
import numpy as np

resim=cv2.imread("hababamSinifi.png")

cv2.rectangle(resim,(455,435),(635,625),[0,0,255],3)

cv2.imshow("Hababam Sinifi",resim)


cv2.waitKey(0)
cv2.destroyAllWindows()