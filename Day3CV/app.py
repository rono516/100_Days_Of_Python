import cv2
# img = cv2.imread('assets/shirt.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('assets/shirt.jpg', 1)  #colored image

# resize image
# img = cv2.resize(img, (400, 400))
# img= cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE) rotate image


cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()