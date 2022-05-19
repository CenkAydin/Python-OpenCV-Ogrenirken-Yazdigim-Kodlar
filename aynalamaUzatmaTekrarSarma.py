import cv2
from cv2 import BORDER_WRAP
from cv2 import BORDER_ISOLATED
from cv2 import BORDER_CONSTANT
import numpy as np

resim=cv2.imread("adileNasit.jpg")

aynalananResim=cv2.copyMakeBorder(resim,75,75,125,125,cv2.BORDER_REFLECT)
uzatilanResim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
tekrarResim=cv2.copyMakeBorder(resim,300,300,300,300,BORDER_WRAP)
sarilanResim=cv2.copyMakeBorder(resim,150,150,150,150,BORDER_CONSTANT,value=(75,150,255))

cv2.imshow("Aynalanan Adile Nasit Fotografi",aynalananResim)
cv2.imshow("Uzatilan Adile Nasit",uzatilanResim)
cv2.imshow("Tekrarlanan Adile Nasit",tekrarResim)
cv2.imshow("Sarilan Adile Nasit",sarilanResim)

cv2.waitKey(0)
cv2.destroyAllWindows()

