import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')


img = cv2.imread('assets/human-1.jpg')
# print(type(img))

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detected_face = face_cascade.detectMultiScale(gray_img, 1.1, 4)  #image and scale factor
# print(faces)

for  (x, y, length,width) in detected_face:
    cv2.rectangle(img, (x, y), (x+length, y+width), (255, 0, 0), 2)


    #cropping, slicing and eye detection
    face_reg_col_roi = img[y:y+width, x:x+length]

    #face region of interest
    face_reg_gray_roi = gray_img[y:y + width, x:x+length]
 
    detectedEye = eye_cascade.detectMultiScale(face_reg_gray_roi, 1.1, 4) 
    
    print(detectedEye)
    for (xe, ye, le,we) in detectedEye:
        cv2.rectangle(face_reg_col_roi, (xe, ye), (xe+le, ye+we), (0,255,0), 7)
    
cv2.imshow('Image', img)


k = cv2.waitKey(17000)

cv2.waitKey()