#
import cv2 as cv

def nothing(x):
    pass

cv.namedWindow('Tracking',cv.WINDOW_NORMAL)

cv.createTrackbar("blue_low_H", "Tracking", 0, 180, nothing)
cv.createTrackbar("blue_low_S", "Tracking", 0, 255, nothing)
cv.createTrackbar("blue_low_V", "Tracking", 0, 255, nothing)
cv.createTrackbar("blue_high_H", "Tracking", 0, 180, nothing)
cv.createTrackbar("blue_high_S", "Tracking", 0, 255, nothing)
cv.createTrackbar("blue_high_V", "Tracking", 0, 255, nothing)

#Blå filter trehshold
#Her defineres tekst farve og størrelse for de blå punkter
blue_font = cv.FONT_HERSHEY_SIMPLEX
blue_fontColor = (255,0,0)
blue_fontScale = .3
blue_lineType= 2
#Her defineres farvefiltret for den blå nuance
blue_low_H = 100
blue_low_S = 100
blue_low_V = 61
blue_high_H = 125
blue_high_S = 199
blue_high_V = 255

window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'
'''
parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
args = parser.parse_args()
cap = cv.VideoCapture(args.camera)
'''
while True:

    # Blå filter trehshold
    # Her defineres tekst farve og størrelse for de blå punkter
    blue_font = cv.FONT_HERSHEY_SIMPLEX
    blue_fontColor = (255, 0, 0)
    blue_fontScale = .3
    blue_lineType = 2
    # Her defineres farvefiltret for den blå nuance
    blue_low_H = cv.getTrackbarPos("blue_low_V", "Tracking")
    blue_low_S = cv.getTrackbarPos("blue_low_V", "Tracking")
    blue_low_V = cv.getTrackbarPos("blue_low_V", "Tracking")
    blue_high_H = cv.getTrackbarPos("blue_high_H", "Tracking")
    blue_high_S = cv.getTrackbarPos("blue_high_S", "Tracking")
    blue_high_V = cv.getTrackbarPos("blue_high_V", "Tracking")

    #ret, frame = cap.read()
   # if frame is None:
     #   break

'''
    # Her oprettes farvefiltre til grøn, blå og rød
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    blue_frame_threshold = cv.inRange(frame_HSV, (blue_low_H,blue_low_S,blue_low_V),(blue_high_H,blue_high_S,blue_high_V))
    #red_frame_threshold = cv.inRange(frame_HSV, (red_low_H,red_low_S,red_low_V),(red_high_H,red_high_S,red_high_V))
    #green_frame_threshold = cv.inRange(frame_HSV, (green_low_H,green_low_S,green_low_V),(green_high_H,green_high_S,green_high_V))
    frame_threshold=(blue_frame_threshold)
    cv.imshow(window_capture_name, frame)
    cv.imshow(window_detection_name, frame_threshold)

'''