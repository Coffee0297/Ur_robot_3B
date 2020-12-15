# C:\Users\Carin\Documents\UCL_2019\3.Sem\Python\UR\testing.py
#
import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0) # eksternt kamera

while(True):
    ret, frame = cap.read()
    # HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # Mask on blue square
    lowerBlue = np.array([101, 56, 141])
    upperBlue = np.array([180, 255, 255])
    maskBlue = cv.inRange(hsv, lowerBlue, upperBlue)
    #
    kernal = np.ones((5, 5), "uint8")
    maskBlue = cv.dilate(maskBlue, kernal)

    # Creating contour to track blue color
    contours, hierarchy = cv.findContours(maskBlue,
                                           cv.RETR_TREE,
                                           cv.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv.boundingRect(contour)
            frame = cv.rectangle(frame, (x, y),
                                (x + w, y + h),
                                (255, 0, 0), 2)

            cv.putText(frame, "Blue Colour", (x, y),
                        cv.FONT_HERSHEY_SIMPLEX, 1.0,
                        (255, 0, 0))

    #mask = cv.inRange(hsv, H_from, H_to)  # mask vælger til og fra hvad vi vil se

    # applying bitwise_and operation
    #res = cv.bitwise_and(img, img, mask=mask)
    #resBlue = cv.bitwise_and(img, img, mask=maskBlue)
    cv.imshow('frame1', frame)

    # Gray
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Webcam', gray)
    # Canny
    canny = cv.Canny(gray, 150, 175)
    cv.imshow('Canny', canny)
    # Laplacian
    lap = cv.Laplacian(gray, cv.CV_64F)
    lap = np.uint8(np.absolute(lap))
    cv.imshow('Laplacian', lap)

    if cv.waitKey(15) == ord('q'):
        break

# cv.waitKey(0)
cap.release()
cv.destroyAllWindows()

