# CBL
#
import numpy as np
import cv2 as cv
import module as mod
# ==================================================================================
# Working with image - object messurement
#webcam = False
#path = 'cap01.jpg'
# ==================================================================================
cap = cv.VideoCapture(0) # eksternt kamera
# ==================================================================================
# Working with image - object messurement
'''
cap.set(10,160) # brightness
cap.set(3,1920) # width
cap.set(4,1080) # hight

while True:
    if webcam:succes, img = cap.read()
    else: img = cv.imread(path)

    mod.getContours(img, showCanny=True)

    img = cv.resize(img,(0,0),None,0.5,0.5)
    cv.imshow('Original', img)
    if cv.waitKey(15) == ord('q'):
        break
'''
# ==================================================================================
# Working with video - Blue square

while(True):
    ret, frame = cap.read()
    frameTest = frame.copy()
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

            cv.putText(frame, "Blue Square", (x, y),
                        cv.FONT_HERSHEY_SIMPLEX, 1.0,
                        (255, 0, 0))

    #mask = cv.inRange(hsv, H_from, H_to)  # mask vælger til og fra hvad vi vil se

    # applying bitwise_and operation
    #res = cv.bitwise_and(img, img, mask=mask)
    #resBlue = cv.bitwise_and(img, img, mask=maskBlue)
    cv.imshow('frame1', frame)


    # *********** Masks *************************
    mod.getContours(frame, show=True)

    #mod.getContours(frameTest, cThr=[100, 100], show=True)

    if cv.waitKey(15) == ord('q'):
        break
'''
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
        
'''
cap.release()
cv.destroyAllWindows()

# ==================================================================================



