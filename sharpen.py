import numpy as np
import cv2

original_image = cv2.imread('colored_car.jpg')

#sharpen kernel
kernel = np.array([[0,-1,0],[-1,9,-1],[0,-1,0]])

sharp_image = cv2.filter2D(original_image,-1,kernel)

cv2.imshow('Original', original_image)
cv2.imshow("Sharpen Image", sharp_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

