# CBL
#from __future__ import print_function
import cv2 as cv
#import argparse
import numpy as np
import defs
#import vision
#import klasser

#img = cv.imread(r'C:\Users\Carin\Documents\UCL_2019\3.Sem\Python\UR\Vision\image_0.png')

# define a video capture object
cam = cv.VideoCapture(0)
# cam.set(10,160)     # 10 for brightness - value 160
# cam.set(3,1920)     # 3 for hight - value 1920
# cam.set(4,1080)     # 4 for width - value 1080
pixToMil = 0.2645833333
scale = 3   # scale to make image bigger
wWorkspace = 200 *scale
hWorkspace = 200 *scale


#-------------------------------------
defs.Capture.takePicture(cam)
original = cv.imread('image_0.png')
#-------------------------------------

#------ Image Processing ----------------------------------
img = defs.Processing.img_copy(original, show=True)
gray = defs.Processing.grayscale(img, show=True)
blur = defs.Processing.blur(gray, show=True)
canny = defs.Processing.canny(blur, show=True)
kernel = defs.Processing.kernel(show=False)
dilated = defs.Processing.dilate(canny, kernel, show=True)
erod = defs.Processing.erode(dilated, kernel, show=True)
print('Done processing')
#----------------------------------------------------------

# save all contours in the variabel 'contours'
finalContours = []      # creating list
Contours = defs.Contours.get_contours(erod, show=False)

defs.Contours.something(img, show=True)




#gray = defs.Processing.grayscale(picture)
# cv.imshow("Picture", gray)
# blur = defs.Processing.blur(gray,show=True)


#frame_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# defs.Processing.get_filter(img, show=True)
#
# print ('getContours2')
# imgContours, fContours = defs.Processing.get_filter(img, show= True, minArea=50000, filter=4)
# # find the biggest objects 4 corners - unsorted
# if len(fContours) != 0:
#     biggest = fContours[0][2]   # takes 1. and 3. parameter in finalContours-->([len(approx), area, approx, bbox, i])
#     print ('Biggest',biggest)
#     imgWarp = defs.Processing.warpImg(img, biggest, wWorkspace, hWorkspace)
#     print('imgWarp',imgWarp.size/3)
#     imgContours2, fContours2 = defs.Processing.get_filter(imgWarp, show=True, showCenterWS=True, findAngle=True, minArea=2000, filter=4, cThr=[60, 60], draw=False)
#
#     if len(fContours) !=0:
#         for obj in fContours2:
#             cv.polylines(imgContours2,[obj[2]], True, (0,255,0),2)  # green full lines
#             nPoints = defs.Processing.reorder(obj[2])    # reorder points
#             print('nPoints reordered: \n ', nPoints)
#
#             # function call to find distance (hight and width of object)
#             nW = round(defs.Processing.findDis(nPoints[0][0] // scale, nPoints[1][0] // scale), 1)    # find width of obj, (number of pixels divided by scale-value)
#             nH = round(defs.Processing.findDis(nPoints[0][0] // scale, nPoints[2][0] // scale), 1)    # find height of obj in millimeters, round to 1 decimal
#             cv.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]),
#                                  (255, 0, 255), 2, 10, 0, 0.08)
#             cv.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
#                                  (255, 0, 255), 2, 10, 0, 0.08)
#             x, y, w, h = obj[3]
#             cv.putText(imgContours2, '{}mm'.format(nW), (x + 30, y - 10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1,
#                              (255,0,255), 1)
#             cv.putText(imgContours2, '{}mm'.format(nH), (x - 70, y + h // 2), cv.FONT_HERSHEY_COMPLEX_SMALL, 1,
#                              (255, 0, 255), 1)
#             print('lllllllllllllllllllllllllllllllllllllllllllllllllllll')
#
#             print('\nWidth: ', nW, '\nHight: ', nH )#, '\nHight: ', {self.height})
#
#     cv.imshow("Workspace", imgContours2)
# # cv.imshow("Last saved image", img)

cv.waitKey(0)
cam.release()
cv.destroyAllWindows()





