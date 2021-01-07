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
        print('HSV values')
        print(self.hl)
        print(self.sl)
        print(self.vl)
        print(self.hh)
        print(self.sh)
        print(self.hv)


green = Color(53,74,66,96,225,185)
blue = Color(0,0,65,171,234,110)
red = Color(0,0,0,24,255,88)
# debugging
green.printPosition()
blue.printPosition()
red.printPosition()


