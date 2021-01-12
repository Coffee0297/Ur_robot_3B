import cv2 as cv
import numpy as np

class Capture:
    def __init__(self, name):
        self.name = name

    def nothing(x):  # definere nothing for at den kan blive ignoreret i cv.createTrackbar
        pass
    # funktionen tager et screenshot fra webcam og gemmer det ---- skal processerer det nu

    def takePicture(cam):
        print('\n------ class Capture -> Function takePicture ------\n')
        cv.namedWindow("Camera test")
        img_counter = 0
        print("Press Escape to close without saving \nPress space to take a picture")
        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv.imshow("Camera test", frame)

            k = cv.waitKey(1)
            if k % 256 == 27:       # wait for ESC key to exit
                # ESC pressed
                print("Escape hit, closing...")
                break

            elif k % 256 == 32:     # wait for SPACE key to exit
                # SPACE pressed
                img_name = "image_{}.png".format(img_counter)
                cv.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                # img_counter += 1   # hvis der skal tages flere billeder

        # cam.release()
        # cv.destroyAllWindows()

# ===================================================================================
class Square:

    def getContours(img, cThr=[150, 175], show=False, showCenterWS=False, findAngle=False, minArea=1000, filter=0, draw=False):  # default parameters
        print('\n------ class Square -> Function getContours ------\n')
        # Do some processing
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)      # convert image to grayscale
        blur = cv.GaussianBlur(gray, (5, 5), 1)         # apply some blur, define kernelsize 5 by 5, sigma 1
        edges = cv.Canny(blur, cThr[0], cThr[1])        # plads 0 og 1 - can be defined by user, otherwise default is 150,175
        kernel = np.ones((5, 5))        # define kernel - returns new 5 by 5 array of ones
        dial = cv.dilate(edges, kernel, iterations=3)   # making thick lines
        erod = cv.erode(dial, kernel, iterations=2)     # making thin lines

        if show:
            # Do some debugging
            cv.imshow('Gray 1st processing', gray)
            cv.imshow('Blur 2nd processing', blur)
            cv.imshow('Edges Canny 3rd processing', edges)
            cv.imshow("Dialate 4th processing", dial)
            cv.imshow("Erode 5th processing", erod)

        # save all contours in the variabel 'contours'
        contours, hiearchy = cv.findContours(erod, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        finalContours = []      # creating list

        # loop through contours
        for i in contours:
            # information about current detected object

            if findAngle:       # get rotational angle of objects in workspace
                for l in range(len(contours)):
                    if contours[l].size > 50:
                        cnt = contours[l]
                        rect = cv.minAreaRect(cnt)

                        print('contours[l].size: ', contours[l].size)
                        print('rect: ', rect[-1])

                        cv.putText(img, str(rect[-1]), (10, 60 + (l * 20)), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255),1)

                        Box = cv.boxPoints(rect)
                        Box = np.int0(Box)

                        cv.drawContours(img, [Box], 0, (255, 255, 0), 1)

            area = cv.contourArea(i)
            print('area: ', area)
            if area > minArea:
                perimeter = cv.arcLength(i, True) #The function computes a curve length or a closed contour perimeter.
                approx = cv.approxPolyDP(i, 0.02 * perimeter, True) #find corner points
                bbox = cv.boundingRect(approx)

                # filter is made if only a certain type of object is wanted, fx a square has 4 cornerpoints
                if filter > 0:
                    if len(approx) == filter:
                        finalContours.append([len(approx), area, approx, bbox, i])
                        print('Long list in finalContours....')
                        print('len(approx)',len(approx))
                        print('Area', area)
                        print('approx', approx)
                        print('bbox',bbox)
                        print('i')
                else:
                    finalContours.append([len(approx), area, approx, bbox, i])


                # calculate x,y coordinates of objects centerpoint
                M = cv.moments(approx)
                x = int(M["m10"] / M["m00"])    # center in pixels on x-axis
                cX = round(x // 3 ,0)           # center in millimeter on x-axis - måske?
                print('X: ', x)
                print('cX: ', cX)

                y = int(M["m01"] / M["m00"])    # center in pixels on y-axis
                cY = round(y // 3 ,0)           # center in millimeter on y-axis - måske?
                print('Y: ', y)
                print('cY: ', cY)


            # define placement of circle and text on image
            if showCenterWS:
                cv.circle(img, (x, y), 5, (0, 0, 0), -1)    # output centerpoint as a dot
                cv.putText(img, str([cX, cY]), (x - 50, y - 35), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 1) # outputs koordinates i mm

        finalContours = sorted(finalContours, key=lambda x: x[1], reverse=True)     # src, len(approx):area, descenting order

        # 'draw' contour-points that we get from findCountour-function
        if draw:
            for con in finalContours:
                cv.drawContours(img,con[4],-1,(0,0,255),3) # dottet red lines, thickness = 3
        return img, finalContours

    # reorder the objects 4 corners - sorted
    def reorder(myPoints):
        print('\n------ class Square -> Function reorder ------\n')
        print(myPoints.shape) # output= (4,1,2), 4 by 1 by 2 (4 values, 1 is redundant, each value has 2 points: x,y
        myPointsNew = np.zeros_like(myPoints) #Return an array of zeros with the same shape and type as a given array.
        myPoints = myPoints.reshape((4, 2)) # removes redundant (the 1)
        add = myPoints.sum(1)   # gets sum of each one of 4 value-sets
        print('add: ', add)
        myPointsNew[0] = myPoints[np.argmin(add)]   # first element, get actual points based on minimum-index
        myPointsNew[3] = myPoints[np.argmax(add)]   # firth element, get actual points based on maximum-index
        diff = np.diff(myPoints, axis=1)            # trækker x fra y
        myPointsNew[1] = myPoints[np.argmin(diff)]  # det tal der er mindst efter diff gemmes her
        myPointsNew[2] = myPoints[np.argmax(diff)]  # det tal der er højst efter diff gemmes her

        print('myPointsNew[0]: ', myPointsNew[0])
        print('myPointsNew[1]: ', myPointsNew[1])
        print('myPointsNew[2]: ', myPointsNew[2])
        print('myPointsNew[3]: ', myPointsNew[3])
        print('myPointsNew Test[3][0][0]: ', myPointsNew[3][0][1])
        return myPointsNew


    def warpImg(img, points, w, h, pad=20):
        print('\n------ class Square -> Function warpImg ------\n')
        print('Workspace points: \n', points)
        points = Square.reorder(points)

        print('Workspace points reordered: \n', points)
        pts1 = np.float32(points)
        pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])   # define pattern
        matrix = cv.getPerspectiveTransform(pts1, pts2)
        imgWarp = cv.warpPerspective(img, matrix, (w, h))
        imgWarp = imgWarp[pad:imgWarp.shape[0] - pad, pad:imgWarp.shape[1] - pad]   # define<-- pad: removes corner-pixels from h + w
        # print('imgWarp: \n',imgWarp)
        return imgWarp

    # returnerer længden på en side
    def findDis(pts1, pts2):
        print('\n------ class Square -> Function finDis ------\n')
        print('pts1, pts2: ', pts1, pts2)
        return ((pts2[0] - pts1[0]) ** 2 + (pts2[1] - pts1[1]) ** 2) ** 0.5 # finder kvadratrod af ((x2-x1)^2 + (y2-y1)^2)


# ===================================================================================

class Circle(Capture):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        self.name = "circle"

    def circum(self):
        return 3.14 * (self.radius + self.radius)

    def getArea(self):
        return 3.14 * self.radius * self.radius

    def printName(self):
        return self.name

