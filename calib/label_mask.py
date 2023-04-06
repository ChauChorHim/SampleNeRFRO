import cv2
import os
import numpy as np

# Define the mouse callback function for drawing on the mask
start_point = None

def draw_line(event, x, y, flags, param):
    global start_point

    if event == cv2.EVENT_LBUTTONDOWN:
        start_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        if start_point is not None:
            cv2.line(mask, start_point, (x, y), (255, 255, 255), 2)
            cv2.line(img, start_point, (x, y), (0, 0, 255), 2)
            start_point = None

# Image path
img_dir = "data/"

# Load the image
img_files = os.listdir(img_dir)
img_files.sort()

# i = 0
for img_file in img_files:
    # if i <= 21:
    #     i += 1
    #     continue
    if img_file.endswith('.png'):
        img = cv2.imread(img_dir + img_file)
    else:
        continue

    # Create a mask with the same dimensions as the image
    mask = np.zeros_like(img)

    # Create a window for the image
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_line)

    while True:
        # Show the original image with the mask overlaid
        masked_image = cv2.addWeighted(img, 0.5, mask, 0.5, 0)
        cv2.imshow('image', masked_image)

        # Wait for a key to be pressed
        key = cv2.waitKey(1)

        # If the 's' key is pressed, save the mask and exit
        if key == ord('s'):
            # Create a copy of the mask to use for filling
            fill_mask = mask.copy()

            # Convert fill_mask to grayscale
            fill_mask = cv2.cvtColor(fill_mask, cv2.COLOR_BGR2GRAY)

            # Find the contours of the mask
            contours, _ = cv2.findContours(fill_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Create a new mask with the same dimensions as the image
            mask = np.zeros_like(img)

            # Fill the region inside the contours
            cv2.fillPoly(mask, contours, (255, 255, 255))

            # Save the mask
            cv2.imwrite(img_dir + "mask_" + img_file, mask)
            break

        # If the 'r' key is pressed, reset the mask
        if key == ord('r'):
            mask = np.zeros_like(img)

        # If the 'c' key is pressed, clear the lines
        if key == ord('c'):
            img = cv2.imread(img_dir + img_file)
            mask = np.zeros_like(img)

    # Clean up and exit
    cv2.destroyAllWindows()
