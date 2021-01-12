import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)
# Video size = (480, 640, 3)
while True:
    ret, img = cap.read()
    blank = np.zeros(img.shape, dtype='uint8')

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    height, width, channels = img.shape

    gaussianblur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
    cv.imshow('gblur', gaussianblur)

    canny = cv.Canny(gaussianblur, 100, 120)
    cv.imshow("Canny", canny)

   





    # cv.imshow("Blank", blank)

    # mask = cv.rectangle(blank, (width//2, height//2),(width//2 - 100, height//2 - 100), (255, 255, 255), -1)
    # cv.imshow("Mask", mask)
    #
    # masked = cv.bitwise_and(gray, gray, mask=mask)
    # cv.imshow("Masked image", masked)

    # cv.imshow("Grå Video", gray)

    # gaussianblur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
    # cv.imshow('gblur', gaussianblur)

    print("Video size: ", img.shape)




    # canny = cv.Canny(gaussianblur,100,120)
    # cv.imshow("Canny", canny)
    #
    #
    # contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    # print(f'{len(contours)} contour(s) found!')





    if cv.waitKey(15) == ord('q'):
        break

img.release()
cv.destroyAllWindows()
