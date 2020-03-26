import cv2
import numpy as np
from mss import mss
from PIL import Image

cords = {'top': 500, 'left': 500, 'width': 200, 'height': 200}
sct = mss()

def mask_circle(img):
    # Convert to grayscale. 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # Blur using 3 * 3 kernel. 
    gray_blurred = cv2.blur(gray, (3, 3)) 
    # Apply Hough transform on the blurred image. 
    detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40) 
    # Draw circles that are detected. 
    if detected_circles is not None: 
        # Convert the circle parameters a, b and r to integers. 
        detected_circles = np.uint16(np.around(detected_circles)) 

        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
            # Draw the circumference of the circle. 
            # cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
            
            # Create a mask
            height, width, depth = img.shape
            circle_img = np.zeros((height, width), np.uint8)
            if r <= 10:
                break
            r -= 10
            cv2.circle(circle_img, (a, b), r, (255, 255, 255), thickness = -1)
            masked_data = cv2.bitwise_and(img, img, mask=circle_img)
            
            # Mask gray colors RGB: (85, 80, 83)
            gray_lo = np.array([40, 40, 40])
            gray_hi = np.array([180, 180, 180])
            mask = cv2.inRange(masked_data, gray_lo, gray_hi)
            masked_data[mask > 0] = (0, 0, 0)
            
            # Mask light blue colors RGB: (157, 236, 250)
            lblue_lo = np.array([150, 150, 100])
            lblue_hi = np.array([255, 255, 200])
            mask = cv2.inRange(masked_data, lblue_lo, lblue_hi)
            masked_data[mask > 0] = (0, 0, 0)
            
            return masked_data, True
    return img, False

def detect_by_arrow(img):
    #convert the image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #apply canny edge detection to the image
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    #show what the image looks like after the application of previous functions
    #perform HoughLines on the image
    lines = cv2.HoughLines(edges,1,np.pi/180,20)
    #create an array for each direction, where array[0] indicates one of the lines and array[1] indicates the other, which if both > 0 will tell us the orientation
    left = [0, 0]
    right = [0, 0]
    up = [0, 0]
    down = [0, 0]
    #iterate through the lines that the houghlines function returned
    for object in lines:
        theta = object[0][1]
        rho = object[0][0]
        #cases for right/left arrows
        if ((np.round(theta, 2)) >= 1.0 and (np.round(theta, 2)) <= 1.1) or ((np.round(theta,2)) >= 2.0 and (np.round(theta,2)) <= 2.1):
            if (rho >= 20 and rho <=  30):
                left[0] += 1
            elif (rho >= 60 and rho <= 65):
                left[1] +=1
            elif (rho >= -73 and rho <= -57):
                right[0] +=1
            elif (rho >=148 and rho <= 176):
                right[1] +=1
        #cases for up/down arrows
        elif ((np.round(theta, 2)) >= 0.4 and (np.round(theta,2)) <= 0.6) or ((np.round(theta, 2)) >= 2.6 and (np.round(theta,2))<= 2.7):
            if (rho >= -63 and rho <= -15):
                up[0] += 1
            elif (rho >= 67 and rho <= 74):
                down[1] += 1
                up[1] += 1
            elif (rho >= 160 and rho <= 171):
                down[0] += 1

    if left[0] >= 1 and left[1] >= 1:
        print("left")
    elif right[0] >= 1 and right[1] >= 1:
        print("right")
    elif up[0] >= 1 and up[1] >= 1:
        print("up")
    elif down[0] >= 1 and down[1] >= 1:
        print("down")

    return (up, down, left, right)

def detect_by_color(img):
    im = Image.fromarray(img)
    colors = im.getcolors(masked_img.shape[0] * masked_img.shape[1]) # RETURNS BGR
    colors = dict(colors)
    color_range = sorted(colors)
    
    if len(color_range) < 2:
        return -1
    
    arrow_color = colors[color_range[-2]]
    if arrow_color == (255, 255, 58):
        arrow_direction = 1 # UP
        print("UP")
    elif arrow_color == (153, 177, 255):
        arrow_direction = 2 # DOWN
        print("DOWN")
    elif arrow_color == (166, 255, 234):
        arrow_direction = 3 # LEFT
        print("LEFT")
    elif arrow_color == (254, 155, 254):
        arrow_direction = 4 # RIGHT
        print("RIGHT")
    else:
        arrow_direction = -1    # None
    
    return arrow_direction

def detect_by_rect(img):
    font = cv2.FONT_HERSHEY_COMPLEX

    im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, threshold = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        cv2.drawContours(im, [approx], 0, (255, 0, 0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        

while(True):
    sct.get_pixels(cords)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    img = np.array(img)
    #img = np.array(Image.open("input_up.png"))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Mask image
    masked_img, found_circle = mask_circle(img)
    
    # Detect direction
    if found_circle:
        color = detect_by_color(masked_img)
        #detect_by_rect(masked_img)
        #detect_by_arrow(masked_img)
    
    cv2.imshow('test', masked_img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break