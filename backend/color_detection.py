import cv2
import numpy as np

averageX = 0

def processImage():
    # this will be a function, called when needed
    image = cv2.imread("opencv_frame.png")
    imageHsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lowerRange = np.array([90,100,89])
    upperRange = np.array([130,255,255])

    mask = cv2.inRange(imageHsv, lowerRange, upperRange)

    contours, hierchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    #note to self - if there aren't anything, return absolutely nothing.
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 1000: #threshold
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 2)
                averageX = x + w/2
                averageX = int(averageX)
                # averageY = y + h/2
                # averageY = int(averageY)

    else:
        pass

    #optionals
    cv2.imshow("Image", image)
    cv2.imshow("Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()