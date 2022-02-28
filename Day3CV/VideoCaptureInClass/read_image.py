import cv2
img = cv2.imread("rono.jpeg", cv2.IMREAD_COLOR)
cv2.imshow("Shadrack", img)
cv2.waitKey(0)
cv2.destroyAllWindows()