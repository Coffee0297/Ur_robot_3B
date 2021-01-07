# tester klasser og objekter
#-------------------------------------------------------
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

    #-------------------------

    # skal nok ligge et andet sted
    def intToStr(self):
        pass

    def strToInt(self):
        pass
#-------------------------------------------------------
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self, x):
        return self.x

    def get_y(self, y):
        return self.y
#-------------------------------------------------------
class Square:
    def __init__(self, width, height, max_points):
        self.width = width
        self.height = height
        self.max_points = max_points
        self.corners = []                           # define a list

    def add_cornerpoints(self, corners):
        if len(self.corners) < self.max_points:     # number of corners
            self.corners.append(corners)            # append to the list
            return True
        return False

    def get_minimum_x_value(self):
        pass

#------------------------------------------------
# create Coordinate objects
k1 = Coordinates(4,1)
k2 = Coordinates(3,1)
k3 = Coordinates(1,3)
k4 = Coordinates(7,3)
# create Square objects
square = Square(2, 2, 4)
# Use method to add 4 point (x,y) to a list
square.add_cornerpoints(k1)
square.add_cornerpoints(k2)
square.add_cornerpoints(k3)
square.add_cornerpoints(k4)
print(square.corners)
print(square.corners[3].x)  # prints out the x-value in the 4th index (in this case 7)
square.corners[0].x
# #------------------------------------------------
# # create Position objects
# homePos = Position(2,4,6,8,10,12)
# p2 = Position(2,2,2,2,2,2)
# p3 = Position(3,3,3,3,3,3)
# p4 = Position(4,4,4,4,4,4)
# #------------------------------------------------
# # debugging
# print(homePos.printPosition())
# print('P2 Position:',p2.printPosition())
# print('P3 Position:',p3.printPosition())
# print('P4 Position:',p4.printPosition())
# #------------------------------------------------
# # using methods
# homePos.addOffset(20)
# print('Home Pos Get Offset:',homePos.getOffset())
# print('Home Position:',homePos.printPosition())
# # - - - - - - - - - - - - - - - - - - - - - - - -
# p4.addOffset(50)
# # de to print herunder gør det samme
# print('P4 Get Offset:',p4.getOffset())
# print('P4 Get Offset:',p4.z)
# # - - - - - - - - - - - - - - - - - - - - - - - -

# b'movej(p[-0.02703978368688221, -0.41162562152534876, 0.3339006287927195, 1.6443410877739137, -2.4824781895547496, 0.8022008840211984])'+ b'
