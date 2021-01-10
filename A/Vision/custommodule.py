import cv2 as cv
import numpy as np

# getContours funktionen
def getContours(img, cThr=[100, 175], showCanny=False, cannyResize=False, minArea = 1000, filter=0, draw = False):
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # Inputbilledet laves til grayscale
    imgBlur = cv.GaussianBlur(imgGray, (5, 5), 1) # Billedet blurres for at fjerne støj - Det grå billede bruges # kernelstørrelsen er 5*5 # sigmaX er en afvigelse på x-aksen så matrixen starter én pixel inde på x-aksen, ellers er det måske talrækken i matrixen som bliver 1?? # sigmaY er standard samme som sigmaX
    imgCanny_Original = cv.Canny(imgBlur, cThr[0], cThr[1]) # Kanterne detekteres - Tager blurred billede som input - Threshold er standard [100,100], men kan ændres af brugeren # Threshold er hvor stor en forskel der skal være på to pixels før den skal reagere på det som en kant.
    imgCanny_Resized = cv.resize(imgCanny_Original.copy(),(0, 0), None, 0.4, 0.4) # Billedet skaleres ned så hele billedet kan ses - Input er canny billedet -
    kernel = np.ones((5,5)) # Laver en matrix med 5*5 rækker af 1-taller - bruges i dilate
    imgDial = cv.dilate(imgCanny_Original, kernel, iterations=3) # Kanterne forstørres i forhold til den mørke baggrund
    imgThres = cv.erode(imgDial, kernel, iterations=2) # Kanterne formindskes igen

    if showCanny: cv.imshow('Canny', imgCanny_Original)
    if cannyResize: cv.imshow('Resized Canny', imgThres)

    contours, hierarchy = cv.findContours(imgThres,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE) # Konturerne findes - RETR_EXTERNAL finder de ydre kanter - De fundne konturer gemmes i contours

    finalContours = [] # En tom liste hvor de færdige og ønskede konturer gemmes
    for i in contours: # Der loopes gennem konturerne i contours for at finde og tegne dem
        area = cv.contourArea(i) # contourArea finder arealet i konturerne "i"
        if area > minArea: # Hvis arealet er større end minArea som standard er 1000 fortsætter processeringen af konturen
            epsilon = cv.arcLength(i,True) # arcLength finder længden på konturen - (selve længden på konturlinjen i pixels) - True betyder at det kun skal være lukkede konturer
            approx = cv.approxPolyDP(i,0.02*epsilon,True) # approxPolyDP tilretter konturlinjen og finder hjørnepunkter - 0.02 er procent ## Skal måske rodes lidt med ##
            # print("Approx", approx)
            bbox = cv.boundingRect(approx) # Der tegnes firkanter om de detekterede konturer

            if filter > 0: # filter er standard 0 - Kan ændres hvis
                if len(approx) == filter:
                    finalContours.append([len(approx),area,approx,bbox,i]) # De ønskede værdier gemmes i listen - [Længden på den tilrettede kontur, arealet i konturen, punkterne i den tilrettede kontur, kontur[i]]
            else:
                finalContours.append([len(approx),area,approx,bbox,i])

    finalContours = sorted(finalContours,key= lambda x:x[1], reverse=True) # Den største kontur i finalContours findes - (listen, key = Hvad der skal sorteres efter - Lambda bruges til at pege på "area" i listen, Reversed = Sorterer fra størst til mindst)

    print("FinalContours", finalContours)

    if draw:
        for con in finalContours:
            cv.drawContours(img,con[4],-1,(0,0,255),7) # Konturerne tegnes på billedet - (billedet, plads nr. 4 i finalContours, farve på konturlinjen, tykkelse på linjen)
            print("Con4",con[4])
    return img, finalContours

def reorder(myPoints):
    # print("myPoints", myPoints.shape)  # Printer: (4,1,2), Det betyder at der er 4 hjørnepunkter som hver har 2 værdier(x,y) - tallet 1 skal ikke bruges til noget og bliver fjernet
    myPointsNew = np.zeros_like(myPoints) # Der laves et array af nuller som matcher myPoints
    myPoints = myPoints.reshape((4,2)) # myPoints laves om til en shape (Tror det er en tuple??) med 4 kolonner og 2 rækker
    # print("myPoints", myPoints)
    add = myPoints.sum(1) # Hver x-y punkt som gemmes i mypoints, lægges sammen
    # print("Add", add)
    # myPointsNew sætter hjørnepunkterne på A4 arket i rigtig rækkefølge
    myPointsNew[0] = myPoints[np.argmin(add)] # Plads 0 i den nye liste af punkter får den mindste sum fra add som bliver 0,0.
    myPointsNew[3] = myPoints[np.argmax(add)] # Plads 3 i den nye liste af punkter får den højeste sum fra add som bliver w,h
    print("myPointsNew[0][0]",myPointsNew[0][0])
    diff = np.diff(myPoints, axis=1) # diff finder differencen mellem punkterne i listen
    # print("Diff",diff)
    myPointsNew[1] = myPoints[np.argmin(diff)] # Plads 1 i den nye liste af punkter bliver w,0
    myPointsNew[2] = myPoints[np.argmax(diff)] # Plads 2 i den nye liste af punkter bliver 0,h

    return myPointsNew # De nye punkter returneres

def warpImg(img, points, w, h, pad = 30): # Ændre pad for at fjerne overflødige kanter på billedet som forstyrrer beregningen af målene
    points = reorder(points)
    pts1 = np.float32(points) # points gemmes i pts1 som float
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]]) # De strukturerede positioner til de nye points
    matrix = cv.getPerspectiveTransform(pts1,pts2) # Der laves en matrix af punkterne
    imgWarp = cv.warpPerspective(img, matrix, (w,h)) # warpPerspective laver et nyt "billede" som har A4-arkets hjørner som grænserne (Billedet indeholder kun A4-arket)
    imgWarp = imgWarp[pad:imgWarp.shape[0]-pad, pad:imgWarp.shape[1]-pad] # Fjerner kanterne på billedet som ikke er en del af arbejdsområdet

    return imgWarp

def findDis(pts1, pts2): # pts1 er x1,y1 og pts2 er x2,y2
    return ((pts2[0]-pts1[0])**2 + (pts2[1]-pts1[1])**2)**0.5 # Pythagoras bruges til at beregne hypotenusen(den ønskede længde) # x2-x1^2 + y2-y2^2 / 0.5 finder hypotenusen


