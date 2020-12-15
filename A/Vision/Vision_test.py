import cv2 as cv
import numpy as np

# Let's load a simple image with 3 black squares
cap = cv.VideoCapture(1)

while True:
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    gaussianblur = cv.GaussianBlur(gray, (5, 5), 0)
    cv.imshow('gblur', gaussianblur)

# Find Canny edges
    edged = cv.Canny(gaussianblur, 30, 200)

# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
    contours, hierarchy = cv.findContours(edged,
    cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    circles = cv.HoughCircles(edged, cv.HOUGH_GRADIENT, 1, 10, np.array([]), 200, 100, 1, 200)
    if circles == 1:
        print('Circle true')
    else:
        print('No circle')


    cv.imshow('Canny Edges After Contouring', edged)


    print("Number of Contours found = " + str(len(contours)))

# Draw all contours
# -1 signifies drawing all contours
    cv.drawContours(img, contours, -1, (0, 255, 0), 3)

    cv.imshow('Contours', img)
    if cv.waitKey(15) == ord('q'):
        break

img.release()
cv.destroyAllWindows()
