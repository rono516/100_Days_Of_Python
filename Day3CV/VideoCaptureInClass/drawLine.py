import numpy as np
import cv2

# Create a black image
# img = np.zeros((512,512,3), np.uint8)
img = cv2.imread("rono.jpeg", cv2.IMREAD_COLOR)

# Draw a diagonal blue line with thickness of 5 px
# img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
#rectangle
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#drawing a circle
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()