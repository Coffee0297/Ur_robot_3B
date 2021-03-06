# ACT
import cv2 as cv
import Functions
import ColorDetection

def main():
    cam = cv.VideoCapture(0)
    # cam.set(10,160)     # 10 for brightness - value 160
    # cam.set(3,1920)     # 3 for hight - value 1920
    # cam.set(4,1080)     # 4 for width - value 1080
    scale = 3  # scale to make image bigger
    wWorkspace = 200 * scale
    hWorkspace = 200 * scale
    w_Klods = 500
    h_Klods = 500

    # -------------------------------------
    # defs.Capture.takePicture(cam)
    img = cv.imread('image_0.png')
    # -------------------------------------

    # --------- Image Processing ------------------------------------
    erod = Functions.Processing.filters(img, cThr=[150, 175], show=False)
    # print('Done processing')
    # ---------------------------------------------------------------

    contours = Functions.Contours.get_contours(erod, show=False)
    # print('\nFinding biggest contour - minArea=50000')
    imgContours, fContours, x, y = Functions.Contours.find_contour(img, contours, minArea=50000, filter=4)

    if len(fContours) != 0:
        biggestContour = fContours[0][
            2]  # takes 1. and 3. parameter in finalContours-->([len(approx), area, approx, bbox, i])
        # print('go to reorder')
        myPoints = Functions.Contours.reorder(biggestContour)
        # print('Finding biggest contour Done')

        # ------ Warp image to define workspace -----------------------------------------
        imgWarp = Functions.Contours.warpImg(img, myPoints, wWorkspace, hWorkspace, show=False)
        # print('imgWarp.size: ', imgWarp.size)
        # print('imgWarp.size/3: ', imgWarp.size/3,'\n')
        # ------ Warp image of object -----------------NY -------------------------------
        imgWarp_copy = imgWarp.copy()

        erodWarp = Functions.Processing.filters(imgWarp_copy, cThr=[150, 60], show=False)
        fContours3 = Functions.Contours.get_contours(erodWarp, show=False)

        # ------- Image Processing on warped image ----------------------
        erod = Functions.Processing.filters(imgWarp, cThr=[150, 60], show=False)
        # cv.imshow("imgContours2/Warped", imgWarp)
        # --------------------------------------------------------------

        contours2 = Functions.Contours.get_contours(erod, show=False)
        # print('\nFind next contour - minArea=2000')
        imgContours2, fContours2, x, y = Functions.Contours.find_contour(imgWarp, contours2, minArea=2000, filter=4,
                                                                         draw=False)

        # --------- Find width and height --------------------------------
        if len(fContours) != 0:
            for obj in fContours2:
                klods1 = fContours3[0][2]
                warpPoints = Functions.Contours.reorder(obj[2])  # reorder points
                # print("KLODS_1: ", klods1)
                imgWarped = Functions.Contours.warpImg(imgWarp_copy, warpPoints, w_Klods, h_Klods, show=False)
                cv.imwrite('image_100.png', imgWarped)

                # print('Farve liste',farve_liste)

                cv.polylines(imgContours2, [obj[2]], True, (0, 255, 0), 2)  # green full lines
                nPoints = Functions.Contours.reorder(obj[2])  # reorder points
                #  print('nPoints reordered: \n ', nPoints)

                # function call to find distance (hight and width of object)
                nW = round(Functions.Contours.findDis(nPoints[0][0] // scale, nPoints[1][0] // scale),
                           1)  # find width of obj, (number of pixels divided by scale-value)
                nH = round(Functions.Contours.findDis(nPoints[0][0] // scale, nPoints[2][0] // scale),
                           1)  # find height of obj in millimeters, round to 1 decimal

                cv.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]),
                               (255, 0, 255), 2, 10, 0, 0.08)
                cv.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
                               (255, 0, 255), 2, 10, 0, 0.08)
                x_, y_, w, h = obj[3]
                cv.putText(imgContours2, '{}mm'.format(nW), (x_ + 30, y_ - 10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1,
                           (255, 0, 255), 1)
                cv.putText(imgContours2, '{}mm'.format(nH), (x_ - 70, y_ + h // 2), cv.FONT_HERSHEY_COMPLEX_SMALL, 1,
                           (255, 0, 255), 1)

                # cv.imshow("imgContours2/Warped", imgContours2)
                # print('\nWidth: ', nW, '\nHight: ', nH )#, '\nHight: ', {self.height})

        # --------- Find Centerpoint -------------------------
        #    defs.Contours.draw_contours(imgContours2,contours2, showCenterWS=True)

        # --------- Find Angle -------------------------
        rad = (Functions.Contours.find_angle(imgContours2, contours2))
        # print('angle list. ', rad)

    else:
        rad = []
        x = []
        y = []
        colorIndex = []
    # -------------------------------------------
    # lav string til robot... returner sidste element fra listerne istedet for hele listen??
    # b'movej(p[-0.02703978368688221, -0.41162562152534876, 0.3339006287927195, 1.6443410877739137, -2.4824781895547496, 0.8022008840211984])'+ b'\n', # Home
    # -------------------------------------------

    colorIndex = ColorDetection.colors(run=True)

    cv.waitKey(0)
    cam.release()
    cv.destroyAllWindows()

    # gå til robot
    # print('program kørt')
    return rad, x, y, colorIndex

# thread.start()
