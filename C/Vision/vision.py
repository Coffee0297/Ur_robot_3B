# tester klasser og objekter
#-------------------------------------------------------
class Color:
    def __init__(self, hl, sl, vl, hh, sh, hv):     # HSV værdier - low/high
        self.hl = hl     # creates atribute called hl and takes in parameter hl
        self.sl = sl
        self.vl = vl
        self.hh = hh
        self.sh = sh
        self.hv = hv

    def printPosition(self):    # til debugging
        print(self.x)
        print(self.y)
        print(self.z)
        print(self.rx)
        print(self.ry)
        print(self.rz)

cv.createTrackbar("green_low_H", "Tracking", 53, 180, nothing)
cv.createTrackbar("green_low_S", "Tracking", 74, 255, nothing)
cv.createTrackbar("green_low_V", "Tracking", 66, 255, nothing)
cv.createTrackbar("green_high_H", "Tracking", 96, 180, nothing)
cv.createTrackbar("green_high_S", "Tracking", 225, 255, nothing)
cv.createTrackbar("green_high_V", "Tracking", 185, 255, nothing)