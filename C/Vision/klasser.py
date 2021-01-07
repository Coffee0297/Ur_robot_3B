# tester klasser og objekter
# Class names staret med stort
# methods_like_this (alt er småt)
# objectsLikeThis (starter med småt)
#-------------------------------------------------------
class Position:
    def __init__(self, x, y, z, rx, ry, rz):
        self.x = x      # creates atribute called x and takes in parameter x
        self.y = y
        self.z = z
        self.rx = rx
        self.ry = ry
        self.rz = rz

    def print_position(self):    # til debugging
        print('Position Coordinates')
        print(self.x)
        print(self.y)
        print(self.z)
        print(self.rx)
        print(self.ry)
        print(self.rz)

    def add_offset(self, z):
        self.z = z

    def get_offset(self):
        return self.z

    #-------------------------

    # skal nok ligge et andet sted
    def int_to_str(self):
        pass

    def str_to_int(self):
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
class Shape:
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

    def get_center_point(self):
        pass

    def get_minimum_x_value(self):
        pass

class Square(Shape):
    def example(self):
        pass

class Circle(Shape):
    def another_example(self):
        pass

#------------------------------------------------
# create Coordinate objects
k1 = Coordinates(1,1)
k2 = Coordinates(5,1)
k3 = Coordinates(1,5)
k4 = Coordinates(5,5)
k5 = Coordinates(0,0)
centerPoint = Coordinates(3,3)

square = Shape(2, 2, 4)     # creates an object with 4 corner points (square)

# Use method to add 4 point (x,y) to a list
print(square.add_cornerpoints(k1))  # prints True (objectno. < maxvalue)
square.add_cornerpoints(k2)
square.add_cornerpoints(k3)
square.add_cornerpoints(k4)
print(square.add_cornerpoints(k5)) # prints False because (objectno. > maxvalue)
print(square.corners)
print(square.corners[3].x)  # prints out the x-value in the 4th index (in this case 7)
square.corners[0].x
#------------------------------------------------
# værdi = 20
# # create Position objects
# homePos = Position(2,4,6,8,10,12)
# p2 = Position(2,2,2,2,2,2)
# p3 = Position(3,3,3,3,3,3)
# p4 = Position(4,4,4,4,4,4)
# #------------------------------------------------
# # debugging
# print(homePos.printPosition())
# print(p2.printPosition())
# print(p3.printPosition())
# print(p4.printPosition())
# #------------------------------------------------
# # using methods
# homePos.add_offset(værdi)
# print('Home Pos Get Offset:',homePos.get_offset())
# print(homePos.printPosition())
# # - - - - - - - - - - - - - - - - - - - - - - - -
# p4.add_offset(50)
# # de to print herunder gør det samme
# print('P4 Get Offset:',p4.get_offset())
# print('P4 Get Offset:',p4.z)
# # - - - - - - - - - - - - - - - - - - - - - - - -

# b'movej(p[-0.02703978368688221, -0.41162562152534876, 0.3339006287927195, 1.6443410877739137, -2.4824781895547496, 0.8022008840211984])'+ b'
