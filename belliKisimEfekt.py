import cv2
import numpy as np

kemalSunal=cv2.imread("kemalSunal.jpg")
#kemalSunal[:,:,0]=255

kemalSunal[150:200,350:500,0]=255
kemalSunal[150:200,350:500,1]=200


cv2.imshow("Kemal Sunal Fotografi",kemalSunal)

cv2.waitKey(0)
cv2.destroyAllWindows()