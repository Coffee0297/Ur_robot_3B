import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)

while True:
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blank = np.zeros(img.shape, dtype='uint8')
    # cv.imshow("Blank", blank)

    mask = cv.circle(blank, (img.shape[1]//2), img.shape[0]//2), 100, 255, -1)
    cv.imshow("Mask", mask)

    masked = cv.bitwise_and(img, img, mask= mask)
    cv.imshow("Masked image", masked)

    # cv.imshow("Grå Video", gray)

    gaussianblur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
    # cv.imshow('gblur', gaussianblur)




    canny = cv.Canny(gaussianblur,100,120)
    cv.imshow("Canny", canny)


    contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    print(f'{len(contours)} contour(s) found!')





    if cv.waitKey(15) == ord('q'):
        break

img.release()
cv.destroyAllWindows()
