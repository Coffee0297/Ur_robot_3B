# Prøv hjørnedetekteringen fra corner detection PDF

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

scale = 3 # Bruges til at lave det færdige A4-vindue(arbejdsområdet) 3 gange større - Ellers ville det være 200*200 pixels
wP = 200 *scale # Bredden på A4-papiret(arbejdsområdet)
hP = 200 *scale # Højden på A4-papiret(arbejdsområdet)


#### While loop ####
while True:

    img = cv.imread(path) # Billedet i path gemmes i "img"

    # img = cv.resize(img, (0,0),None,0.5,0.5) # Skalerer img til halv størrelse

    img, conts = cm.getContours(img, minArea=5000, cannyResize= True, filter=4, draw=True) # Funktionens færdigprocesserede billede returneres til "img". - finalContours returneres til "conts". - minArea sættes til 5000 for kun at detektere store objekter på billedet - filter sættes til 4 for kun at få objekter med over 4 hjørner.

    if len(conts) != 0:
        biggest = conts[0][2] # Plads [0] peger på den største kontur i listen "approx". - Plads[2] peger på listen "approx" i finalContours
        # print("Biggest: ", biggest)
        imgWarp = cm.warpImg(img, biggest, wP, hP) # imgWarp

        img2, conts2 = cm.getContours(imgWarp, minArea=500, filter=4, cThr=[50,50], draw=False, findCenter=True) # minArea er standard 2000
        # Hjørnerne af de fundne objekter i arbejdsområdet, bruges til at måle højden og bredden på objektet

        if len(conts2) != 0: # tjekker at der er fundet konturer
            for obj in conts2: # Der arbejdes med hvert objekt der detekteres
                print("Objekt",obj)
                cv.polylines(img2, [obj[2]], True,(0,255,0), 2) # Polylines tegner en kant om objektet # obj[2] indeholder punkterne
                nPoints = cm.reorder(obj[2]) # punkterne sættes i korrekt rækkefølge
                nW = round((cm.findDis(nPoints[0][0]//scale,nPoints[1][0]//scale)/10),3) # afstanden mellem 0,0 [0][0] og w,0 [1][0] . # antallet af pixels divideres med scale for at få de korrekte mål # Outputtet ville blive i mm, men ved at dividere med 10 bliver det i cm. # Round gør at det kun bliver tal med ét decimal round("-",1). #
                nH = round((cm.findDis(nPoints[0][0]//scale,nPoints[2][0]//scale)/10),3) # afstanden mellem 0,0 [0][0] og h,0 [2][0] . # antallet af pixels divideres med scale for at få de korrekte mål # Outputtet ville blive i mm, men ved at dividere med 10 bliver det i cm. # Round gør at det kun bliver tal med ét decimal round("-",1). #
                print("nPoints",nPoints[0][0][0], nPoints[0][0][1], "Punkt 2",nPoints[2][0][0],nPoints[2][0][1])
                cv.arrowedLine(img2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]),
                               (255, 0, 255), 3, 8, 0, 0.05) # arrowLine tegner en pil mellem punkterne # [0][0][0] = 235(x), [0][0][1] = 202(y), [1][0][0] = 358(x), [1][0][1] = 202(y)
                cv.arrowedLine(img2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
                               (255, 0, 255), 3, 8, 0, 0.05) # arrowLine tegner en pil mellem punkterne # [0][0][0] = 235(x), [0][0][1] = 202(y), [2][0][0] = 233(x), [2][0][1] = 323(y)
                x, y, w, h = obj[3]
                print("x",x,"y",y,"w",w,"h",h)
                print("Objekt[3]",obj[3])
                print("nW",nW,"nH",nH)
                cv.putText(img2, '{}cm'.format(nW), (x + 30, y - 10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1,
                           (255, 0, 255), 1)
                cv.putText(img2, '{}cm'.format(nH), (x - 70, y + h // 2), cv.FONT_HERSHEY_COMPLEX_SMALL, 1,
                           (255, 0, 255), 1)
        cv.imshow("A4", img2)

    img = cv.resize(img,(0,0),None, 0.4, 0.4)

    cv.imshow("Original", img)

    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break
cap.release()
cv.destroyAllWindows()