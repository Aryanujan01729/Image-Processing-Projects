import cv2
import numpy as np

def solution(image_path):
    ############################
    ############################
    # Load the image
    image = cv2.imread(image_path)
  # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise (optional but often recommended)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Apply the Canny edge detector
    edges = cv2.Canny(blurred_image, threshold1=30, threshold2=100)  # Adjust threshold values as needed
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)
    bisector=[]
    print(len(lines))

    if lines is not None:
        for rho, theta in lines[:, 0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            a=int(a)
            b=int(b)
            #print("RGB Value at ({}, {}): {}".format(a, b,image[a,b] ))
            bisector.append((x1,y1))
            bisector.append((x2,y2))
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 225), 2)  # Draws the line in black (BGR format)
    # Display the image with detected lines
    #cv2.imshow('Image with Lines', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    (x1,y1)=bisector[0]
    (x2,y2)=bisector[1]
    (x3,y3)=bisector[2]
    (x4,y4)=bisector[3]
    mid_x1=((x1+x3)/2)
    mid_x2=((x2+x4)/2)
    mid_y1=((y1+y3)/2)
    mid_y2=((y2+y4)/2)
    dy=(mid_y2-mid_y1)
    dx=(mid_x2-mid_x1)

    

    # Display the image with detected circles
    #cv2.imshow('Detected Circles', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()



    angle_radian = np.arctan2(dy, dx)
    angle_degrees = np.degrees(angle_radian)
    if angle_degrees <0:
        angle_degrees=180+angle_degrees
        
    print((angle_degrees))
    mid_x1=int(mid_x1)
    mid_x2=int(mid_x2)
    mid_y1=int(mid_y1)
    mid_y2=int(mid_y2)

    cv2.line(image,(mid_x1,mid_y1) , (mid_x2,mid_y2), (0, 0, 0), 2)  # Draws the line in black (BGR format)

    '''cv2.imshow('Angle Bisector Line', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''

    image = image_path
    img = cv2.imread(image)

    # Get the image dimensions
    height, width = img.shape[:2]
    width=width+200
    height=height+200

    # Define the rotation angle in degrees (e.g., 45 degrees)
    angle = angle_degrees

    # Calculate the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/3), angle, 1)

    # Apply the rotation to the image
    rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))

    # Display the rotated image

    ############################
    ############################
    ## comment the line below before submitting else your code wont be executed##
    # pass
    return rotated_image
