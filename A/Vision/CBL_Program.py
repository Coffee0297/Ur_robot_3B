# CBL
from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np
import CBL_defs as defs
import CBL_vision as vision

# define a video capture object
cam = cv.VideoCapture(0, cv.CAP_DSHOW)
# cam.set(10,160)     # 10 for brightness - value 160
# cam.set(3,1920)     # 3 for hight - value 1920
# cam.set(4,1080)     # 4 for width - value 1080
pixToMil = 0.2645833333
scale = 3   # scale to make image bigger
wWorkspace = 200 *scale
hWorkspace = 200 *scale
w_Klods = 200 *scale
h_Klods = 200 *scale

defs.Capture.takePicture(cam)
img = cv.imread('image_1.png')
#img = cv.imread(r'C:\Users\Carin\Documents\UCL_2019\3.Sem\Python\UR\Vision\image_20.png')

frame_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

defs.Square.getContours(img, show=True)

imgContours, fContours = defs.Square.getContours(img, show= True, showCenterWS=True, minArea=50000, filter=4)

farve_liste = []

#centerx = x
#centery = y
# print('X: ', centerx)
# print('Y: ', centery)
#print('Exit getContours',imgContours)
# find the biggest objects 4 corners - unsorted
if len(fContours) != 0:
    biggest = fContours[0][2]   # takes 1. and 3. parameter in finalContours-->([len(approx), area, approx, bbox, i])
    print ("BIGGEST",biggest)
    imgWarp = defs.Square.warpImg(img, biggest, wWorkspace, hWorkspace)
    print("GAMMELWARP",imgWarp)
    print(imgWarp.size/3)

    imgWarp_copy = imgWarp.copy()

    imgContours2, fContours2 = defs.Square.getContours(imgWarp, show=True, showCenterWS=True, findAngle=True, minArea=2000, filter=4, cThr=[60, 60], draw=False)



    imgContours3, fContours3 = defs.Square.getContours(imgWarp_copy, show=True, showCenterWS=False, findAngle=False, minArea=2000, filter=4, cThr=[60, 60], draw=False)



    # print("FUNDNE KONTURER",fContours2)
    if len(fContours) !=0:

        # Hver klods på billedet gemmes i en klods-variabel
        for obj in fContours2:
            klods1 = fContours2[0][2]
            klods2 = fContours2[1][2]
            klods3 = fContours2[2][2]
            print("KLODS_1: ", klods1)
            print("KLODS_2: ", klods2)
            print("KLODS_3: ", klods3)

            # Klodserne warpes med warpfunktionen
            ny_imgWarp1 = defs.Square.warpImg(imgWarp_copy, klods1, w_Klods, h_Klods)
            ny_imgWarp2 = defs.Square.warpImg(imgWarp_copy, klods2, w_Klods, h_Klods)
            ny_imgWarp3 = defs.Square.warpImg(imgWarp_copy, klods3, w_Klods, h_Klods)

            cv.imshow("KLODS1", ny_imgWarp1)
            cv.imshow("KLODS2", ny_imgWarp2)
            cv.imshow("KLODS3", ny_imgWarp3)

            # colorchannels puttes i farve
            farve1 = ny_imgWarp1[0][2]
            farve2 = ny_imgWarp2[0][2]
            farve3 = ny_imgWarp3[0][2]


            print("FARVE KLODS 1 BGR: ", farve1)
            print("FARVE KLODS 2 BGR: ", farve2)
            print("FARVE KLODS 3 BGR: ", farve3)

            # Hver detekteret colorchannel puttes i listen farve_liste
            farve_liste.append(farve1)
            farve_liste.append(farve2)
            farve_liste.append(farve3)
            print("Farveliste før del: ", farve_liste)

            print("FARVELISTE1", farve_liste[0])
            print("FARVELISTE2", farve_liste[1])
            print("FARVELISTE3", farve_liste[2])

            cv.polylines(imgContours2,[obj[2]], True, (0,255,0),2)  # green full lines
            nPoints = defs.Square.reorder(obj[2])    # reorder points
            print("OBJ[2]",obj[2])
            print('nPoints reordered: \n ', nPoints)

            # function call to find distance (hight and width of object)
            nW = round(defs.Square.findDis(nPoints[0][0] // scale, nPoints[1][0] // scale), 1)    # find width of obj, (number of pixels divided by scale-value)
            nH = round(defs.Square.findDis(nPoints[0][0] // scale, nPoints[2][0] // scale), 1)    # find height of obj in millimeters, round to 1 decimal
            cv.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]),
                                 (255, 0, 255), 2, 10, 0, 0.08)
            cv.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
                                 (255, 0, 255), 2, 10, 0, 0.08)
            x, y, w, h = obj[3]
            cv.putText(imgContours2, '{}mm'.format(nW), (x + 30, y - 10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1,
                             (255,0,255), 1)
            cv.putText(imgContours2, '{}mm'.format(nH), (x - 70, y + h // 2), cv.FONT_HERSHEY_COMPLEX_SMALL, 1,
                             (255, 0, 255), 1)

            print('\nWidth: ', nW, '\nHight: ', nH)

    print("FARVELISTE ANTAL AF FARVER",len(farve_liste)//3)
    print("FARVELISTE", farve_liste)

    # Der tælles op i farvelisten og farven printes
    for f in range(len(farve_liste)//3):
        if max(farve_liste[f]) == farve_liste[f][0]:

            print("Farven er blå")

        elif max(farve_liste[f]) == farve_liste[f][1]:
            print("Farven er grøn")

        elif max(farve_liste[f]) == farve_liste[f][2]:
            print("Farven er rød")

    print("farve_liste",farve_liste)
    print("WarpIMG_SIZE", imgWarp.shape)
    cv.imshow("Workspace", imgContours2)


cv.waitKey(0)
cam.release()
cv.destroyAllWindows()





