import cv2
cap = cv2.VideoCapture(0) 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output12.avi',fourcc, 20.0, (640,480)) 
                                        #(20) frames per second       #size/number of frames(640, 480)
while(cap.isOpened()): 
    ret, frame = cap.read()
    if ret==True: 
        flippedframe = cv2.flip(frame,1)
        out.write(flippedframe)
        cv2.imshow('VideoOfFlippedFrame',flippedframe)
        key = cv2.waitKey(10) #number of miliseconds waited for next event
        if key == 27:  
            break
        else:
            break
        
cap.release()
out.release()     