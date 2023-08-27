import numpy as np
import cv2

def findCenter(timeStep):
    # Read the image
    image = cv2.imread('./screenshots/Screenshot_{}.png'.format(timeStep))

    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range of blue color in HSV
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Threshold the HSV image to get only blue colors
    bmask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find contours and process the blue mask
    bcontours, _ = cv2.findContours(bmask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cartx, carty = None, None

    for contour in bcontours:
        M = cv2.moments(contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
			# Center x position relative to image width
            cartx = cx - image.shape[1] / 2
            carty = cy
            break  # Only process the first contour

    # Convert the image to grayscale for pole detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
    ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY_INV)

    # Find contours for pole detection
    contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    polex, poley = None, None

    for contour in contours:
        M = cv2.moments(contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            polex, poley = cx, cy
            break  # Only process the first contour

    if cartx is None or polex is None:
        return None, None  # Return None if either cart or pole not detected

    # Calculate theta (angle of the pendulum)
    if polex == (cartx + image.shape[1] / 2):
        theta = 0
    else:
        theta = np.pi / 2 - np.arctan(np.abs((poley - carty) / (polex - (cartx + image.shape[1] / 2))))

    # Draw contours and centers on the image
    cv2.drawContours(image, bcontours, -1, (0, 255, 0), 2)
    cv2.circle(image, (int(cartx + image.shape[1] / 2), carty), 7, (0, 0, 255), -1)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    cv2.circle(image, (polex, poley), 7, (0, 0, 255), -1)

    # Save the image with contours and centers
    cv2.imwrite("./detection/image_{}.png".format(timeStep), image)

    return cartx, theta