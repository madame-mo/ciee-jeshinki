import cv2

# Read an image
img = cv2.imread('image.jpg')

# Display the image in a window
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
