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

# ======================================================================================================================

class Processing:
    def img_copy(self,show=False):
        print('Program Runing......')
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

    def canny(self, a, b, show=False):    # canny edges cThr=[150, 175]
        print('...Canny')
        # cThr1 = 175               # treshhold 1
        # cThr2 = 75                # treshhold 2
        canny = cv.Canny(self, a, b)  # plads 0 og 1 - can be defined by user, otherwise default is 150,175
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

# ======================================================================================================================

class Contours:
    def get_contours(self, show=False):
        print('\n------ Contour -> Function get_contour ------\nGetting Contours.....')
        contours, hiearchy = cv.findContours(self, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        if show:
            print('Contours: ', contours)
        return contours
# ----------------------------------------------------------------------------------------------------------------------
    def find_contour(self, contours,  minArea=2000, filter=0, draw=False):
        print('\n------ Contour -> Function find_contour ------\nFinding Contours.....')
        finalContours = []  # creating list
        # loop through contours
        for i in contours:
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
                        print('4 cornerpoints detected....')
                    else:
                        print('Shape with '"{}".format(filter),'corners, is added to th list "finalContours"')
                        finalContours.append([len(approx), area, approx, bbox, i])
                else:
                    print('No contour is added to the list "finalContours"')

            # 'draw' contour-points that we get from findCountour-function
        if draw:
            for j in finalContours:
                cv.drawContours(self, j[filter], -1, (0, 0, 255), 3)  # dottet red lines, thickness = 3

        finalContours = sorted(finalContours, key=lambda x: x[1], reverse=True)     # src, len(approx):area, descenting order
        return self, finalContours

# ----------------------------------------------------------------------------------------------------------------------
# +++++++++++++++++++++++++++++++++++++++
    def warpImg(self, points, w, h, pad=20, show=False):
        print('\n------ Contour -> Function warpImg ------\n')
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
        print('\n------ Contour -> Function reorder ------\n')
        print('Points not ordered: \n',myPoints)
        print(myPoints.shape) # output= (4,1,2), 4 by 1 by 2 (4 values, 1 is redundant, each value has 2 points: x,y
        myPointsNew = np.zeros_like(myPoints) #Return an array of zeros with the same shape and type as a given array.
        myPoints = myPoints.reshape((4, 2)) # removes redundant (the 1)
        add = myPoints.sum(1)   # gets sum of each one of 4 value-sets
        print('add: ', add)
        myPointsNew[0] = myPoints[np.argmin(add)]   # first element, get actual points based on minimum-index
        myPointsNew[3] = myPoints[np.argmax(add)] # firth element, get actual points based on maximum-index
        diff = np.diff(myPoints, axis=1)
        myPointsNew[1] = myPoints[np.argmin(diff)]
        myPointsNew[2] = myPoints[np.argmax(diff)]
        print('Points ordered: \n')
        print('myPointsNew[0]: ', myPointsNew[0])
        print('myPointsNew[1]: ', myPointsNew[1])
        print('myPointsNew[2]: ', myPointsNew[2])
        print('myPointsNew[3]: ', myPointsNew[3])
        return myPointsNew
#+++++++++++++++++++++++++++++++++++++++
# ----------------------------------------------------------------------------------------------------------------------
# # ----------------------------------------------------------------------------------------------------------------------
# # +++++++++++++++++++++++++++++++++++++++
#     def warpImg(self, points, w, h, pad=20, show=False):
#         print('\n------ Contour -> Function warpImg ------\n')
#         print('Workspace points: \n', points)
#         points = Contours.reorder(points)
#
#         print('Points reordered: \n', points)
#         pts1 = np.float32(points)
#         pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])   # define pattern
#         matrix = cv.getPerspectiveTransform(pts1, pts2)
#         imgWarp = cv.warpPerspective(self, matrix, (w, h))
#         imgWarp = imgWarp[pad:imgWarp.shape[0] - pad, pad:imgWarp.shape[1] - pad]   # define<-- pad: removes corner-pixels from h + w
#         # print('imgWarp: \n',imgWarp)
#         if show:
#             cv.imshow('Workspace Image: \n',imgWarp)
#         return imgWarp
# # ----------------------------------------------------------------------------------------------------------------------
#     def reorder(myPoints):
#         print('\n------ Contour -> Function reorder ------\n')
#         print(myPoints.shape) # output= (4,1,2), 4 by 1 by 2 (4 values, 1 is redundant, each value has 2 points: x,y
#         myPointsNew = np.zeros_like(myPoints) #Return an array of zeros with the same shape and type as a given array.
#         myPoints = myPoints.reshape((4, 2)) # removes redundant (the 1)
#         add = myPoints.sum(1)   # gets sum of each one of 4 value-sets
#         print('add: ', add)
#         myPointsNew[0] = myPoints[np.argmin(add)]   # first element, get actual points based on minimum-index
#         myPointsNew[3] = myPoints[np.argmax(add)] # firth element, get actual points based on maximum-index
#         diff = np.diff(myPoints, axis=1)
#         myPointsNew[1] = myPoints[np.argmin(diff)]
#         myPointsNew[2] = myPoints[np.argmax(diff)]
#
#         print('myPointsNew[0]: ', myPointsNew[0])
#         print('myPointsNew[1]: ', myPointsNew[1])
#         print('myPointsNew[2]: ', myPointsNew[2])
#         print('myPointsNew[3]: ', myPointsNew[3])
#         return myPointsNew
# #+++++++++++++++++++++++++++++++++++++++
# # ----------------------------------------------------------------------------------------------------------------------



    # def draw_contours(self, finalContours, showCenterWS=False):
    #     for con in finalContours:
    #         cv.drawContours(self,con[4],-1,(0,0,255),3) # dottet red lines, thickness = 3
    #
    #     M = cv.moments(approx)
    #     x = int(M["m10"] / M["m00"])  # center in pixels on x-axis
    #     cX = round(x // 3, 0)  # center in millimeter on x-axis - måske?
    #     print('Centerpoint X: ', cX)
    #
    #     y = int(M["m01"] / M["m00"])  # center in pixels on y-axis
    #     cY = round(y // 3, 0)  # center in millimeter on y-axis - måske?
    #     print('Centerpoint Y: ', cY)
    #
    #     # define placement of circle and text on image
    #     if showCenterWS:
    #         cv.circle(self, (x, y), 5, (0, 0, 0), -1)  # output centerpoint as a dot
    #         cv.putText(self, str([cX, cY]), (x - 50, y - 35), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0),
    #                    1)  # outputs koordinates i mm
    #     return self


    #reorder the objects 4 corners - sorted






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

