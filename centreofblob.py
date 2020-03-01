import cv2
import numpy as np

img = cv2.imread('1.png')
img = np.asarray(img, dtype=np.uint8)
# convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# convert the grayscale image to binary image
ret,thresh = cv2.threshold(gray_image,50,255,0)

# find contour in the binary image
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#for c in contours:
 #   M = cv2.moments(c)
  #  if M["m00"]!=0:
   #     cX = int(M["m10"] / M["m00"])
    #    cY = int(M["m01"] / M["m00"])
     #   print(cX,cY)
    #else:
     #   cX,cY=0,0
    
for c in contours:
	# calculate moments for each contour
    M = cv2.moments(c)
    if M["m00"]!=0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        print(cX,cY)
    else:
        cX,cY=0,0
	# calculate x,y coordinate of center
    cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
    cv2.putText(img, "centroid", (cX, cY ),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
# display the image
cv2.imshow("Image", img)
cv2.waitKey(0)

# 3.4.1 im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# 3.2.0 im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 	
