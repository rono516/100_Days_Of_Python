import cv2 as cv

face_cascade = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_eye.xml')

image = cv.imread('assets/human-1.jpg')
print(type(image))
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
detectedFace = face_cascade.detectMultiScale(gray_image, 1.1, 4)


print(detectedFace)
for (x, y, length, width) in detectedFace:
    cv.rectangle(image, (x, y), (x + length, y + width), (255, 0, 0), 10)

    #Cropping/Slicing Eye detection
    face_reg_col_roi = image[y:y+width, x:x+length]
    face_reg_gray_roi = gray_image[y:y + width, x:x + length] 
    detectedEyes = eye_cascade.detectMultiScale(face_reg_gray_roi, 1.1, 4)
    print(detectedEyes)

    for(xe, ye, lengthe, widthe) in detectedEyes:
        cv.rectangle(face_reg_col_roi, (xe, ye), (xe + lengthe, ye + widthe), (0, 255, 0), 7)
  


cv.imshow('Face Detection', image)

k = cv.waitKey(17000)


cv.destroyAllWindows()