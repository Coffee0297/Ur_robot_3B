import cv2 as cv
import numpy as np
#import vision

# ===================================================================================
class Capture:
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
class Processing:
    def img_copy(self,show=False):
        print('__init__')
        print('Processing......')
        img = self.copy()
        if show:
            cv.imshow("Original Image", img)
        return img

    def grayscale(self, show=False):
        print('...Grayscale')
        img = cv.cvtColor(self, cv.COLOR_BGR2GRAY)  # convert image to grayscale
        if show:
            cv.imshow("Gray", img)
        return img

    def blur(self, show=False):
        print('...Blur')
        kSize1 = 5     # define kernelsize - fx 5 by 5
        kSize2 = 5
        sigmaX = 1
        blur = cv.GaussianBlur(self, (kSize1, kSize2), sigmaX)  # applying some blur
        if show:
            cv.imshow("Blur", blur)
        return blur

    def canny(self, show=False):    # canny edges
        print('...Canny')
        cThr1 = 175               # treshhold 1
        cThr2 = 75                # treshhold 2
        canny = cv.Canny(self, cThr1, cThr2)  # plads 0 og 1 - can be defined by user, otherwise default is 150,175
        if show:
            cv.imshow("Canny", canny)
        return canny

    def kernel(show=False):
        print('...Kernel')
        kernel = np.ones((5, 5))            # define kernel - returns new 5 by 5 array of ones
        if show:
            cv.imshow("Kernel", kernel)
        return kernel

    def dilate(self, kernel, show=False):
        print('...Dilate')
        #kernel = np.ones((5, 5))
        dilated = cv.dilate(self, kernel, iterations=2)  # making thick lines
        if show:
            cv.imshow("dilate", dilated)
        return dilated

    def erode(self, kernel, show=False):
        print('...Erode')
        erod = cv.erode(self, kernel, iterations=1)  # making thin lines
        if show:
            cv.imshow("erod", erod)
        return erod


#---------
class Contours:
    def get_contours(self, show=False):
        print('Finding Contours.....')
        contours, hiearchy = cv.findContours(self, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        if True:
            print('Contours: ', contours)
        return contours

    defs.Square.getContours(img, show=True)
    imgContours, fContours = defs.Square.getContours(img, show=True, minArea=50000, filter=4)
#print('Final Contours is put in descenting order')
    def something(self):
        # loop through contours
        for i in contours:
            # information about current detected object
            findAngle = True
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
                        print('FinalContours')
                else:
                    finalContours.append([len(approx), area, approx, bbox, i])


                # calculate x,y coordinates of objects centerpoint
                M = cv.moments(approx)
                x = int(M["m10"] / M["m00"])    # center in pixels on x-axis
                cX = round(x // 3 ,0)           # center in millimeter on x-axis - måske?
                print('cX: ', cX)

                y = int(M["m01"] / M["m00"])    # center in pixels on y-axis
                cY = round(y // 3 ,0)           # center in millimeter on y-axis - måske?
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

    #reorder the objects 4 corners - sorted

#---------
    # def reorder(myPoints):
    #     print('\n------ class Square -> Function reorder ------\n')
    #     print(myPoints.shape) # output= (4,1,2), 4 by 1 by 2 (4 values, 1 is redundant, each value has 2 points: x,y
    #     myPointsNew = np.zeros_like(myPoints) #Return an array of zeros with the same shape and type as a given array.
    #     myPoints = myPoints.reshape((4, 2)) # removes redundant (the 1)
    #     add = myPoints.sum(1)   # gets sum of each one of 4 value-sets
    #     print('add: ', add)
    #     myPointsNew[0] = myPoints[np.argmin(add)]   # first element, get actual points based on minimum-index
    #     myPointsNew[3] = myPoints[np.argmax(add)] # firth element, get actual points based on maximum-index
    #     diff = np.diff(myPoints, axis=1)
    #     myPointsNew[1] = myPoints[np.argmin(diff)]
    #     myPointsNew[2] = myPoints[np.argmax(diff)]
    #
    #     print('myPointsNew[0]: ', myPointsNew[0])
    #     print('myPointsNew[1]: ', myPointsNew[1])
    #     print('myPointsNew[2]: ', myPointsNew[2])
    #     print('myPointsNew[3]: ', myPointsNew[3])
    #     return myPointsNew

#---------

    # def warpImg(img, points, w, h, pad=20):
    #     print('\n------ class Square -> Function warpImg ------\n')
    #     print('Workspace points: \n', points)
    #     points = Processing.reorder(points)
    #
    #     print('Workspace points reordered: \n', points)
    #     pts1 = np.float32(points)
    #     pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])   # define pattern
    #     matrix = cv.getPerspectiveTransform(pts1, pts2)
    #     imgWarp = cv.warpPerspective(img, matrix, (w, h))
    #     imgWarp = imgWarp[pad:imgWarp.shape[0] - pad, pad:imgWarp.shape[1] - pad]   # define<-- pad: removes corner-pixels from h + w
    #     # print('imgWarp: \n',imgWarp)
    #     return imgWarp

    # returnerer længden på en side

#-------

    # def findDis(pts1, pts2):
    #     print('\n------ class Square -> Function finDis ------\n')
    #     print('pts1, pts2: ', pts1, pts2)
    #     return ((pts2[0] - pts1[0]) ** 2 + (pts2[1] - pts1[1]) ** 2) ** 0.5 # finder kvadratrod af ((x2-x1)^2 + (y2-y1)^2)

# ===================================================================================

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

