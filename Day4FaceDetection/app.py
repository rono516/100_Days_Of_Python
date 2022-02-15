import cv2
img = cv2.imread('assets/jonte.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('jonte', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("cannot read frame")
            
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow("frame", gray)
        
        if cv2.waitKey(1) == ord('q'):
            
            break
        
cap.release()
cv2.destroyAllWindows()        