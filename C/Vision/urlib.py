# tester klasser og objekter
class Position:
    def __init__(self, x, y, z, rx, ry, rz):
        self.x = x      # creates atribute called x and takes in parameter x
        self.y = y
        self.z = z
        self.rx = rx
        self.ry = ry
        self.rz = rz

    def printPosition(self):    # til debugging
        print(self.x)
        print(self.y)
        print(self.z)
        print(self.rx)
        print(self.ry)
        print(self.rz)

    def addOffset(self, z):
        self.z = z

    def getOffset(self):
        return self.z

    def intToStr(self):
        pass

    def strToInt(self):
        pass

#------------------------------------------------
# create objects
homePos = Position(2,4,6,8,10,12)
p2 = Position(2,2,2,2,2,2)
p3 = Position(3,3,3,3,3,3)
p4 = Position(4,4,4,4,4,4)
#------------------------------------------------
# debugging
print(homePos.printPosition())
print('P2 Position:',p2.printPosition())
print('P3 Position:',p3.printPosition())
print('P4 Position:',p4.printPosition())
#------------------------------------------------
# using methods
homePos.addOffset(20)
print('Home Pos Get Offset:',homePos.getOffset())
print('Home Position:',homePos.printPosition())
# - - - - - - - - - - - - - - - - - - - - - - - -
p4.addOffset(50)
# de to print herunder gør det samme
print('P4 Get Offset:',p4.getOffset())
print('P4 Get Offset:',p4.z)
# - - - - - - - - - - - - - - - - - - - - - - - -

# b'movej(p[-0.02703978368688221, -0.41162562152534876, 0.3339006287927195, 1.6443410877739137, -2.4824781895547496, 0.8022008840211984])'+ b'
