import cv2
import numpy as np

original_image = cv2.imread('colored_car.jpg', cv2.IMREAD_COLOR)
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

'''
# Laplacian kernel
kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])

# -1 is the destination depth
result_name = cv2.filter2D(gray_image,-1,kernel)
'''
result_image = cv2.Laplacian(gray_image,-1)
# instead of the above , there is an inbuilt method to use for edge detection

cv2.imshow('Original', gray_image)
cv2.imshow("Result Image", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



