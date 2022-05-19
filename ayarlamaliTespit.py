import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H","Trackbars",0,180,nothing)
cv2.createTrackbar("L-S","Trackbars",0,255,nothing)
cv2.createTrackbar("L-V","Trackbars",0,255,nothing)
cv2.createTrackbar("U-H","Trackbars",180,180,nothing)
cv2.createTrackbar("U-H","Trackbars",255,255,nothing)
cv2.createTrackbar("U-H","Trackbars",255,255,nothing)



while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([160,50,50])
    upper_red = np.array([180,255,255])
    
    mask = cv2.inRange(hsv,lower_red,upper_red)

    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
 