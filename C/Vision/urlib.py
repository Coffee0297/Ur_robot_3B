# tester klasser og objekter
class Position:
    def __init__(self, x, y, z, rx, ry, rz):
        self.x = x      # creates atribute called x
        self.y = y
        self.z = z
        self.rx = rx
        self.ry = ry
        self.rz = rz

    def addOffset(self, z):
        self.z = z

    def newOffset(self):
        return self.z

    def intToStr(self):
        pass

    def strToInt(self):
        pass

homePos = Position(2,4,6,8,10,12)
homePos.addOffset(20)
print(homePos.newOffset())


# homePos.x is equal to the object which is a (build in)-type 'int' with the value of 2

# debugging
print(homePos)
print(homePos.x)
print(homePos.y)
print(homePos.z)
print(homePos.rx)
print(homePos.ry)
print(homePos.rz)
# b'movej(p[-0.02703978368688221, -0.41162562152534876, 0.3339006287927195, 1.6443410877739137, -2.4824781895547496, 0.8022008840211984])'+ b'
