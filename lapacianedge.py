import cv2
 
# Read the original image
img = cv2.imread('racecar2.jpg') 
# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)
 
# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)  
# Laplacian Edge Detection
laplacian = cv2.Laplacian(img_blur,cv2.CV_64F)
# Display Laplacian Edge Detection Image
cv2.imshow('Laplacian Edge Detection', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()