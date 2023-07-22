import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Code for color-based object detection.')
parser.add_argument('--image', help='Path to image file.', default='./image.jpg')
args = parser.parse_args()

# Load the image
image = cv2.imread('./images/avatares.jpg')

# Convert the image to the HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the color range for the color to detect
# These bounds need to be adjusted according to the color you want to detect
lower_color_bounds = np.array([0, 0, 0])
upper_color_bounds = np.array([0, 0, 255])

# Apply the color mask to the image
color_mask = cv2.inRange(hsv_image, lower_color_bounds, upper_color_bounds)

# Find the contours in the color mask
contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the detected objects on the image
for contour in contours:
    cv2.drawContours(image, contour, -1, (0, 255, 0), 3)

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
