from __future__ import print_function
import cv2 as cv
import numpy as np
import custommodule as cm
import fsm

webcam = True # Tænd og sluk for kameraet - Er kameraet slukket, vil processeringen foregå med billedet i path
cap = cv.VideoCapture(0, cv.CAP_DSHOW) # Forbind til webcamet - cv.CAP_DSHOW starter kameraet hurtigere
fsm.Shape.takePicture(cap) # Funktionen tager cap som input og når der trykkes "space", tages der et stillbillede som gemmes i Visionmappen. Trykkes der escape starter processeringen af stillbilledet.
path = 'c:\\Users\\Pc\\PycharmProjects\\Ur_robot_3B\\A\\Vision\\image_0.png' # Stillbilledet fra webcamet gemmes i path

# cap.set's første position refererer til et ID på en parameter der kan ændres
cap.set(10,160) # Position 10 er Lysstyrke (brightness) - TÆNKER IKKE DET ER RELEVANT!!!!??
cap.set(3,1920) # Position 3 er Bredde
cap.set(4,1080) # Position 4 er Højde
scale = 3
wP = 200 *scale
hP = 200 *scale


#### While loop ####
while True:

    webcam = False

    if webcam: success,img = cap.read()
    else: img = cv.imread(path)

    img, conts = cm.getContours(img, minArea=5000, cannyResize= True, filter=4, draw=True)

    if len(conts) != 0:
        biggest = conts[0][2]
        print("Biggest: ", biggest)
        imgWarp = cm.warpImg(img, biggest, wP, hP)
        img2, conts2 = cm.getContours(imgWarp, minArea=200, filter=4, cThr=[50,50], draw=True) # minArea er standard 2000
        if len(conts2) != 0:
            for obj in conts2:
                cv.polylines(img2, [obj[2]], True,(0,255,0), 2)
                nPoints = cm.reorder(obj[2])
                nW = round((cm.findDis(nPoints[0][0]//scale,nPoints[1][0]//scale)/10),1)
                nH = round((cm.findDis(nPoints[0][0]//scale,nPoints[2][0]//scale)/10),1)
                cv.arrowedLine(img2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]),
                               (255, 0, 255), 3, 8, 0, 0.05)
                cv.arrowedLine(img2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
                               (255, 0, 255), 3, 8, 0, 0.05)
                x, y, w, h = obj[3]
                cv.putText(img2, '{}cm'.format(nW), (x + 30, y - 10), cv.FONT_HERSHEY_COMPLEX_SMALL, 2,
                           (255, 0, 255), 2)
                cv.putText(img2, '{}cm'.format(nH), (x - 70, y + h // 2), cv.FONT_HERSHEY_COMPLEX_SMALL, 2,
                           (255, 0, 255), 2)
        cv.imshow("A4", img2)


    img = cv.resize(img,(0,0),None, 0.4, 0.4)




    cv.imshow("Original", img)

    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break
cap.release()
cv.destroyAllWindows()