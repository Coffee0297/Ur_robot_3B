import cv2 as cv
import numpy as np
#import vision

# ===================================================================================

class Capture:
    def takePicture(cam):
        print('\n------ class Capture -> Function takePicture ------')
        cv.namedWindow("Camera test")
        img_counter = 0
        print("\nPress Escape to close without saving \nPress space to take a picture")
        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv.imshow("Camera test", frame)

            k = cv.waitKey(1)
            if k % 256 == 27:       # wait for ESC key to exit
                # ESC pressed
                print("Escape hit, closing...\n")
                break

            if k % 256 == 27:       # wait for T key to exit
                # T pressed
                print("Use Trackbar to find HSV-values, press return to finish...\n")


            elif k % 256 == 32:     # wait for SPACE key to exit
                # SPACE pressed
                img_name = "image_{}.png".format(img_counter)
                cv.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                # img_counter += 1   # hvis der skal tages flere billeder

        # cam.release()
        # cv.destroyAllWindows()

# ======================================================================================================================

class Processing:
    def filters(self, cThr=[150, 175], show=False):  # default parameters
        print('\n------ Processing -> Function --> Filters ------\nApplaying masks.....\n')
        # Do some processing
        gray = cv.cvtColor(self, cv.COLOR_BGR2GRAY)      # convert image to grayscale
        blur = cv.GaussianBlur(gray, (5, 5), 1)         # apply some blur, define kernelsize 5 by 5, sigma 1
        edges = cv.Canny(blur, cThr[0], cThr[1])        # plads 0 og 1 - can be defined by user, otherwise default is 150,175
        kernel = np.ones((5, 5))        # define kernel - returns new 5 by 5 array of ones
        dilated = cv.dilate(edges, kernel, iterations=3)   # making thick lines
        erod = cv.erode(dilated, kernel, iterations=2)     # making thin lines
        print('Processing......')
        print('...Grayscale')
        print('...Blur')
        print('...Canny')
        print('...Kernel')
        print('...Dilated')
        print('...Erode')
        if show:
            # Do some debugging
            #cv.imshow('Gray 1st processing', gray)
            #cv.imshow('Blur 2nd processing', blur)
            cv.imshow('Edges Canny 3rd processing', edges)
            cv.imshow("Dialate 4th processing", dilated)
            cv.imshow("Erode 5th processing", erod)

        return erod
# ======================================================================================================================

class Contours:
    def get_contours(self, show=False):
        print('\n------ Contour -> Function get_contour ------\nGetting Contours.....\n')
        contours, hiearchy = cv.findContours(self, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        if show:
            print('Contours: ', contours)
        return contours
# ----------------------------------------------------------------------------------------------------------------------
    def find_contour(self, contours,  minArea=2000, filter=0, draw=False, showCenterWS=True):
        print('------ Contour -> Function find_contour ------\nFinding Contours.....')
        finalContours = []  # creating list
        # loop through contours
        for i in contours:
            area = cv.contourArea(i)
            print('Contour found:  Area =', area)
            if area > minArea:
                perimeter = cv.arcLength(i, True) #The function computes a curve length or a closed contour perimeter.
                approx = cv.approxPolyDP(i, 0.02 * perimeter, True) #find corner points
                bbox = cv.boundingRect(approx)

                # filter is made if only a certain type of object is wanted, fx a square has 4 cornerpoints
                if filter > 0:
                    if len(approx) == filter:
                        finalContours.append([len(approx), area, approx, bbox, i])
                        print("{}".format(filter),' cornerpoints detected....')
                    else:
                        print('Shape with '"{}".format(filter),'corners, is added to th list "finalContours"')
                        finalContours.append([len(approx), area, approx, bbox, i])
                else:
                    print('No contour is added to the list "finalContours"')

                # calculate x,y coordinates of objects centerpoint
                M = cv.moments(approx)
                x = int(M["m10"] / M["m00"])    # center in pixels on x-axis
                cX = round(x / 2.8, 5)          # center in millimeter on x-axis
                centerXMeters = cX / 1000       # center in meter on x-axis
                print('X: ', x)
                print('cX: ', cX)

                y = int(M["m01"] / M["m00"])    # center in pixels on y-axis
                cY = round(y / 2.8, 5)          # center in millimeter on y-axis
                centerYMeters = cY / 1000       # center in meter on y-axis
                print('Y: ', y)
                print('cY: ', cY)


        finalContours = sorted(finalContours, key=lambda x: x[1],reverse=True)  # src, len(approx):area, descenting order

        # 'draw' contour-points that we get from findCountour-function
        if draw:
            for con in finalContours:
                cv.drawContours(self, con[4], -1, (0, 0, 255), 3)  # dottet red lines, thickness = 3

        return self, finalContours
# ----------------------------------------------------------------------------------------------------------------------
    def find_angle(self, contours2):
        # get rotational angle of objects in workspace
        for i in contours2:
            area = cv.contourArea(i)
            for l in range(len(contours2)):
                if contours2[l].size > 50:
                    cnt = contours2[l]
                    rect = cv.minAreaRect(cnt)

                    print('contours[l].size: ', contours2[l].size)
                    print('rect: ', rect[-1])

                    cv.putText(self, str(rect[-1]), (10, 60 + (l * 20)), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255),1)

                    Box = cv.boxPoints(rect)
                    Box = np.int0(Box)

                    cv.drawContours(self, [Box], 0, (255, 255, 0), 1)
# ----------------------------------------------------------------------------------------------------------------------
    def warpImg(self, points, w, h, pad=20, show=False):
        print('\n------ Contour -> Function warpImg ------')
        pts1 = np.float32(points)
        pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])   # define pattern
        matrix = cv.getPerspectiveTransform(pts1, pts2)
        imgWarp = cv.warpPerspective(self, matrix, (w, h))
        imgWarp = imgWarp[pad:imgWarp.shape[0] - pad, pad:imgWarp.shape[1] - pad]   # define<-- pad: removes corner-pixels from h + w
        # print('imgWarp: \n',imgWarp)
        if show:
            cv.imshow('Workspace Image: \n',imgWarp)
        return imgWarp
# ----------------------------------------------------------------------------------------------------------------------
    def reorder(myPoints):
        print('\n------ Contour -> Function reorder ------')
        print('Points not ordered:\n',myPoints)
        #print(myPoints.shape) # output= (4,1,2), 4 by 1 by 2 (4 values, 1 is redundant, each value has 2 points: x,y
        myPointsNew = np.zeros_like(myPoints) #Return an array of zeros with the same shape and type as a given array.
        myPoints = myPoints.reshape((4, 2)) # removes redundant (the 1)
        add = myPoints.sum(1)   # gets sum of each one of 4 value-sets
        print('\nadd: ', add)
        myPointsNew[0] = myPoints[np.argmin(add)]   # first element, get actual points based on minimum-index
        myPointsNew[3] = myPoints[np.argmax(add)] # firth element, get actual points based on maximum-index
        diff = np.diff(myPoints, axis=1)
        myPointsNew[1] = myPoints[np.argmin(diff)]
        myPointsNew[2] = myPoints[np.argmax(diff)]
        print('\nPoints ordered: ')
        print('myPointsNew[0]: ', myPointsNew[0])
        print('myPointsNew[1]: ', myPointsNew[1])
        print('myPointsNew[2]: ', myPointsNew[2])
        print('myPointsNew[3]: ', myPointsNew[3])
        return myPointsNew
# ----------------------------------------------------------------------------------------------------------------------
#     def draw_contours(self, finalContours, aprox):
        # for con in finalContours:
        #     cv.drawContours(self,con[4],-1,(0,0,255),3) # dottet red lines, thickness = 3

        # M = cv.moments(approx)
        # x = int(M["m10"] / M["m00"])  # center in pixels on x-axis
        # cX = round(x // 3, 0)  # center in millimeter on x-axis - måske?
        # print('Centerpoint X: ', cX)
        #
        # y = int(M["m01"] / M["m00"])  # center in pixels on y-axis
        # cY = round(y // 3, 0)  # center in millimeter on y-axis - måske?
        # print('Centerpoint Y: ', cY)
        #
        # #define placement of circle and text on image
        # if showCenterWS:
        #     cv.circle(self, (x, y), 5, (0, 0, 0), -1)  # output centerpoint as a dot
        #     cv.putText(self, str([cX, cY]), (x - 50, y - 35), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0),1) #outputs koordinates i mm
        #
        # return self
# ----------------------------------------------------------------------------------------------------------------------
    def findDis(pts1, pts2):
        print('\n------ class Square -> Function finDis ------\n')
        print('pts1, pts2: ', pts1, pts2)
        return ((pts2[0] - pts1[0]) ** 2 + (pts2[1] - pts1[1]) ** 2) ** 0.5 # finder kvadratrod af ((x2-x1)^2 + (y2-y1)^2)



class Circle():
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

