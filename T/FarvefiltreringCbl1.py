import cv2
import numpy as np

#img = cv2.imread(r'C:\Users\Carin\Documents\UCL_2019\3.Sem\Python\pyBilleder\robot_arm.jpg')

def nothing(x): 
    pass
  
# Vinduesnavn
cv2.namedWindow('Tracking') 
  
# Opretter en trackbar og attaches  
# vedhæfter det til vindue
cv2.createTrackbar("Hue Low", "Tracking", 0, 180, nothing)                    
cv2.createTrackbar("Saturation Low", "Tracking", 0, 255, nothing)                    
cv2.createTrackbar("Value Low", "Tracking", 0, 255, nothing)                     
cv2.createTrackbar("Hue High", "Tracking", 0, 180, nothing)                     
cv2.createTrackbar("Saturation High", "Tracking", 0, 255, nothing)                     
cv2.createTrackbar("Value High", "Tracking", 0, 255, nothing)
                      
cap = cv2.VideoCapture(0) # eksternt kamera

# En uendelig løkke.
while True:       
    _, img = cap.read() # _-variablen betyder false or true (kamera tændt eller ej)
      
    # Konverterer billeder fra BGR til HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                      
    # find LH trackbar position 
    l_h = cv2.getTrackbarPos("Hue Low", "Tracking")                            
    # find LS trackbar position 
    l_s = cv2.getTrackbarPos("Saturation Low", "Tracking")                            
    # find LV trackbar position 
    l_v = cv2.getTrackbarPos("Value Low", "Tracking")                            
    # find HH trackbar position 
    h_h = cv2.getTrackbarPos("Hue High", "Tracking")                             
    # find HS trackbar position 
    h_s = cv2.getTrackbarPos("Saturation High", "Tracking")                             
    # find HV trackbar position 
    h_v = cv2.getTrackbarPos("Value High", "Tracking")                             
    # create a given numpy array (low)
    H_from = np.array([l_h, l_s, l_v])                    
    # create a given numpy array (high)
    H_to = np.array([h_h, h_s, h_v])
    
    # værdierne for den røde klods
    lowerRed = np.array([0, 95, 123])
    upperRed = np.array([15, 255, 255])
    maskRed = cv2.inRange(hsv, lowerRed, upperRed)

    # værdierne for den grønne klods
    lowerGreen = np.array([45, 77, 97])
    upperGreen = np.array([99, 255, 255])
    maskGreen = cv2.inRange(hsv, lowerGreen, upperGreen)

    # værdierne for den blå klods
    lowerBlue = np.array([101, 56, 141])
    upperBlue = np.array([180, 255, 255])
    maskBlue = cv2.inRange(hsv, lowerBlue, upperBlue)

    # # værdierne for den gul klods
    # lowerYellow = np.array([27, 91, 118])
    # upperYellow = np.array([88, 255, 255])
    # maskYellow = cv2.inRange(hsv, lowerYellow, upperYellow)

    # Morphological Transform, Dilation 
    # for each color and bitwise_and operator 
    # between imageFrame and mask determines 
    # to detect only that particular color
    kernal = np.ones((5, 5), "uint8")

    # For red color
    maskRed = cv2.dilate(maskRed, kernal) 
      
    # For green color
    maskGreen = cv2.dilate(maskGreen, kernal) 
      
    # For blue color 
    maskBlue = cv2.dilate(maskBlue, kernal)   
                              
    # Creating contour to track red color 
    contours, hierarchy = cv2.findContours(maskRed, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
      
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            img = cv2.rectangle(img, (x, y),  
                                       (x + w, y + h),  
                                       (0, 0, 255), 2) 
              
            cv2.putText(img, "Red Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, 
                        (0, 0, 255))

    #cv2.imshow('MaskRed', maskRed)


    # Creating contour to track green color 
    contours, hierarchy = cv2.findContours(maskGreen, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
      
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            img = cv2.rectangle(img, (x, y),  
                                       (x + w, y + h),  
                                       (0, 255, 0), 2) 
              
            cv2.putText(img, "Green Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, 
                        (0, 255, 0))

    #cv2.imshow('MaskGreen', maskGreen)


    # Creating contour to track blue color 
    contours, hierarchy = cv2.findContours(maskBlue, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
      
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            img = cv2.rectangle(img, (x, y),  
                                       (x + w, y + h),  
                                       (255, 0, 0), 2) 
              
            cv2.putText(img, "Blue Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, 
                        (255, 0, 0))

    #cv2.imshow('MaskGreen', maskGreen)

    mask = cv2.inRange(hsv, H_from, H_to)  # mask vælger til og fra hvad vi vil se
                         
    # applying bitwise_and operation 
    res = cv2.bitwise_and(img, img, mask = mask) 
    resRed = cv2.bitwise_and(img, img, mask = maskRed)
    # resBlue = cv2.bitwise_and(img, img, mask = maskBlue)
    # resGreen = cv2.bitwise_and(img, img, mask = maskGreen)
    # resYellow = cv2.bitwise_and(img, img, mask = maskYellow) 
                         
      
    # display frame, mask 
    # and res window 
    cv2.imshow('frame', img) 
    # cv2.imshow('mask', mask) 
    # cv2.imshow('res', res) 
    # cv2.imshow('Res Red', resRed) 
    # cv2.imshow('Res Blue', resBlue)
    # cv2.imshow('Res Green', resGreen)
    # cv2.imshow('Res Yellow', resYellow)
          
    # break out of while loop 
    # Tryk på q
    if cv2.waitKey(15) == ord('q'):
        break
         
# release the captured frames  
# img.release()
  
# Destroys all windows.  
cv2.destroyAllWindows() 