import numpy as np
import cv2 as cv

#initiate video
cap = cv.VideoCapture('outputmyvideo.avi')

#listener
while(cap.isOpened()):
    ret, frame = cap.read()
    cv.imshow('frameVideoTitle', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):    
        break
cap.release()
cv.destroyAllWindows()
