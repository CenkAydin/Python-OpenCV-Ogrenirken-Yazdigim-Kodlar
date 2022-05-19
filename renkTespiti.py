import re
import cv2
import numpy as np

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1,)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #red
    lower_red = np.array([160,50,50])
    upper_red = np.array([180,255,255])
    red_mask = cv2.inRange(hsv_frame,lower_red,upper_red)
    red = cv2.bitwise_and(frame, frame, mask= red_mask)
    

    #orange
    ORANGE_MIN = np.array([5, 50, 50],np.uint8)
    ORANGE_MAX = np.array([15, 255, 255],np.uint8)
    orange_mask = cv2.inRange(hsv_frame,ORANGE_MIN,ORANGE_MAX)
    orange = cv2.bitwise_and(frame,frame, mask = orange_mask)

    #blue
    lower_blue = np.array([110,50,50],np.uint8)
    upper_blue = np.array([130,255,255],np.uint8)
    blue_mask = cv2.inRange(hsv_frame,lower_blue,upper_blue)
    blue = cv2.bitwise_and(frame,frame, mask = blue_mask)

    #yellow
    lower_yellow = np.array([22, 93, 0], dtype="uint8")
    upper_yellow = np.array([45, 255, 255], dtype="uint8")
    yellow_mask = cv2.inRange(hsv_frame,lower_yellow,upper_yellow)

    #for (x,y,w,h) in blue_mask:
    #   cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 4)


    cv2.imshow("Webcam",frame)


    #red
    #cv2.imshow("Red Mask", red_mask)
    #cv2.imshow("Red",red)
    
    #orange
    #cv2.imshow("Orange Mask",orange_mask)
    #cv2.imshow("Orange",orange)
    
    #blue
    #cv2.imshow("Blue",blue)
    cv2.imshow("Blue Mask",blue_mask)

    #yellow
    #cv2.imshow("Yellow Mask",yellow_mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
    
        break

cap.release()
cv2.destroyAllWindows()
