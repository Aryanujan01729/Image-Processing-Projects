import cv2
import numpy as np

# Usage
def solution(image_path):
    ######################################################################
    ######################################################################
    #####  WRITE YOUR CODE BELOW THIS LINE ###############################
    image= cv2.imread(image_path)
    width, height = 600, 600
    flag = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background (BGR format)

    # Define colors
    orange = (51,153,255)  # BGR value for orange
    green = (0, 128, 0)     # BGR value for green
    navy = (255, 0, 0)      # BGR value for navy blue
    white = (255, 255, 255) # BGR value for white

    # Draw orange rectangle
    cv2.rectangle(flag, (0, 0), (600, 200), orange, -1)

    # Draw green rectangle
    cv2.rectangle(flag, (0, 200), (600, 400), white, -1)

    # Draw big blue circle
    cv2.circle(flag, (300, 300),100, navy, -1)

    # Draw big white circle
    cv2.circle(flag, (300, 300),98, white, -1)

    # # Draw mini blue circles
    # for i in range(24):
    #     angle = 15 * i
    #     x = int(300 + 100 * np.cos(np.radians(angle)))
    #     y = int(300 + 100 * np.sin(np.radians(angle)))
    #     cv2.circle(image, (x, y), 1, navy, -1)

    # # Draw small blue circle
    # cv2.circle(image, (300, 300), 20, navy, -1)

    # Draw spokes
    for i in range(24):
        angle = 15 * i
        x1 = int(300 + 98 * np.cos(np.radians(angle)))
        y1 = int(300 + 98 * np.sin(np.radians(angle)))
        x2 = 300
        y2 = 300
        cv2.line(flag, (x1, y1), (x2, y2), navy, 1)
    # Draw green rectangle
    cv2.rectangle(flag, (0, 400), (600,600), green, -1)
    '''cv2.imshow('Rotated Image', flag)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
    length=image.shape[0]
    breath=image.shape[1]
    color_change1 = 0
    color_change2 = 0
    saffron=[51,153,225]
    white=[225,225,225]
    green=[0,128,0]
    # Initialize color2 and i before the loop
    black =[0,0,0]
    pat1=""
    pat2=""
    # Loop through a range of values for i
    for j in range(0,breath,10):
        for i in range(0,length,10):
            color1 = image[i,j]
            if (all(abs(p1 - p2) == 0 for p1, p2 in zip(color1, black))):
                continue
            if (all((abs(p1 - p2) == 0 or abs(p1 - p2) == 30)  for p1, p2 in zip(color1, saffron))):
                if pat1.count('s')==0:
                    pat1=pat1+"s"
                if pat2.count('s')==0:
                    pat2=pat2+"s"
            if (all(abs(p1 - p2) == 30 for p1, p2 in zip(color1, white))):
                #print("white")
                if pat1.count('w')==0:
                    pat1=pat1+"w"
                if pat2.count('w')==0:
                    pat2=pat2+"w"
            if (all(abs(p1 - p2) == 0 for p1, p2 in zip(color1, green))):
                if pat1.count('g')==0:
                    #print("green")
                    pat1=pat1+"g"
                if pat2.count('g')==0:
                    pat2=pat2+"g"
        if pat1=="swg":
            return flag
            '''cv2.imshow('Indian Flag',flag)
            cv2.waitKey(0)
            cv2.destroyAllWindows()'''
            break
        if pat1=="gws":
            rotated_image = cv2.rotate(flag, cv2.ROTATE_180)
            return rotated_image
            '''cv2.imshow('Indian Flag',rotated_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()'''
            break
        if pat2=="swg":
            rotated_image = cv2.transpose(flag)
            rotated_image = cv2.flip(rotated_image, 0)# 0 indicates vertical flip
            return rotated_image
            # Display or save the rotated image
            '''cv2.imshow('Rotated Image', rotated_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()'''
            break
        if pat2=="gws":
            rotated_image = cv2.transpose(flag)
            rotated_image = cv2.flip(rotated_image, 1)  # 1 indicates horizontal flip
            return  rotated_image
            # Display or save the rotated image
            '''cv2.imshow('Rotated Image', rotated_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()'''
            break 
        pat1=""
        
    
    
        
        
            
            
            
            
    
    
        











    ######################################################################
