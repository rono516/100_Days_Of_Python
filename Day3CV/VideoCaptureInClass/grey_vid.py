import numpy as np
import cv2 as cv

#initiate video
cap = cv.VideoCapture('outputmyvideo.avi')

#listener
while(cap.isOpened()):
    ret, frame = cap.read()
    # cv.imshow('frameVideoTitle', frame)
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray Scale", gray)
    if cv.waitKey(100) & 0xFF == ord('q'):    
        break
cap.release()
cv.destroyAllWindows()
