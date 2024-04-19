# Jai Hind : Drone Positioner

The national fag holds signifcant cultural and symbolic importance for a nation. It serves asa powerul emblem that embodies the history, values, unity of a country via evoking a sense of patriotism and pride. Flags are more than mere pieces of cloth; they are visual representationso a nation’s identity.During aerial maneuvers, UAV or drones have to position themselves by controlling tilt andheight. Experimental robotics use ArUco markers (you can consider them as QR codes) whichare placed on the grounds or adjusting their position. However, fxed size visual patterns can beused in remote terrain for drone positioning. Indian fag serves as a good localizer by militarydrones. At the current non-optimal position, drone sees the image as shown in ‘input’, then itadjusts its position (tilt and height) continuously with minimum movement till it sees the fnal‘reerence’ image. Note there is no need o rotation along Z-(height)-axis (yaw). Your task is togenerate the ‘reference’ image or the input seen by drone.
Your function should take input as an image array and it should return the output as animage array. Here input size may vary but each reerence image is having a size 600x600 pixels,radius of circle = 100, center of circle is (300,300), circle width = 2 and spoke width = 1 pixel. Youwill be given the python program, where you have to complete the unction while returning theproper reference image for each input image. There will be 10 to 20 test cases used or automaticevaluation of your program. Think about all corner cases.
# INPUT

1) ![1](https://github.com/Aryanujan01729/Image-Processing-Projects/assets/139656147/9dacdcc0-1573-4ec3-b896-7803ef8df8d7)    
2) ![4](https://github.com/Aryanujan01729/Image-Processing-Projects/assets/139656147/d43be3c2-22c3-4a75-ac7b-d051a4f53b7a)


# OUTPUT
1) ![1](https://github.com/Aryanujan01729/Image-Processing-Projects/assets/139656147/3804c873-d356-450b-8806-48c3b5ec8e0e)
2) ![4](https://github.com/Aryanujan01729/Image-Processing-Projects/assets/139656147/4fa42263-f417-436c-b4e6-aefa3613e929)

# Anuprasth Drishyam: Horizontal Viewer

Indian ancient Sanskrit literature holds a wealth o knowledge, encrypted in the language thatmodern society is not uent in. To digitize this knowledge, we need to scan the images and thenuse optical character recognition (OCR), an image processing algorithms to digitize it. However,many times, the scanned images are not horizontally aligned, which causes OCR to ail or pro-duce erroneous digitization. These scanned images need to be re-rotated so that the fnal textappears perectly aligned horizontally in a readable orm.Design a python program to realign scanned text always in horizontal viewing manner. Fig. 3shows some o inputs and corresponding output or these images. Your program will be testedon various dierent input images where in the output any text character should not be cut andimage should be horizontally alinged. Output image size can be dierent than input image size

# INPUT 
1)  ![3_b](https://github.com/Aryanujan01729/Image-Processing-Projects/assets/139656147/9f2cf963-abd1-4bbd-bd66-2cc9fa27799f)


# OUTPUT
![Screenshot 2024-04-19 193416](https://github.com/Aryanujan01729/Image-Processing-Projects/assets/139656147/197f9481-d86c-41f5-a5cd-b15fc48d9c97)




