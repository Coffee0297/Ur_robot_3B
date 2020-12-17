import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)
# Video size = (480, 640, 3)
while True:
    ret, img = cap.read()
    ret, thresh = cv.threshold(img, 127, 255,0)
    im2, contours, hierarchy = cv.findContours(thresh, 1, 2)

    cnt = contours[0]
    M = cv.moments(cnt)
    print("M: ",M)

    cx = int(M['m10']/M['m00'])
    cx = int(M['m01'] / M['m00'])

    area = cv.contourArea(cnt)

    perimeter = cv.arcLength(cnt,True)

    rect = cv.minAreaRect(cnt)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    cv.drawContours(img,[box],0,(0,0,255),2)

    cv.imshow("Test", img)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    height, width, channels = img.shape



    if cv.waitKey(15) == ord('q'):
        break

img.release()
cv.destroyAllWindows()
