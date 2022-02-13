import cv2
#read image
img = cv2.imread('assets/003.jpg', cv2.IMREAD_COLOR)
#resize image
img = cv2.resize(img , (400, 400))

#display image
cv2.imshow('Image', img)

#wait an infinite amount of time
cv2.waitKey(0)
#destroy window on click of any button
cv2.destroyAllWindows()