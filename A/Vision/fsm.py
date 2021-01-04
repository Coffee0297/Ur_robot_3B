# CBL
import cv2 as cv
import numpy as np

class Shape:
    def __init__(self, name):
        self.name = name

    def nothing(x):  # definere nothing for at den kan blive ignoreret i cv.createTrackbar
        pass
    # funktionen tager et screenshot fra webcam og gemmer det ---- skal processerer det nu
    def takePicture(cam):
        cv.namedWindow("test")
        img_counter = 0
        print("Press Escape to close \nPress space to take a picture")
        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv.imshow("test", frame)

            k = cv.waitKey(1)
            if k % 256 == 27:       # wait for ESC key to exit
                # ESC pressed
                print("Escape hit, closing...")
                break

            elif k % 256 == 32:     # wait for SPACE key to exit
                # SPACE pressed
                img_name = "image_{}.png".format(img_counter)
                cv.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                # img_counter += 1   # hvis der skal tages flere billeder

        cam.release()
        cv.destroyAllWindows()

# ===================================================================================
# class Square(Shape):
#     def __init__(self, name, a, b):
#         super().__init__(name)
#         self.a = a
#         self.b = b
#         self.name = "square"
#
#
#     def getContours(img, cThr=[150, 175], show=False):
#         # Do some processing
#         gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#         blur = cv.GaussianBlur(gray, (5, 5), 1)
#         edges = cv.Canny(blur, cThr[0], cThr[1])  # plads 0 og 1
#         kernel = np.ones((5, 5))
#         dial = cv.dilate(edges, kernel, iterations=3)
#         erod = cv.erode(dial, kernel, iterations=2)
#
#         #count = erod.copy()
#
#         if show:
#             # Do some debugging
#             cv.imshow('Gray 1', gray)
#             cv.imshow('Blur 2', blur)
#             cv.imshow('Edges Canny 3', edges)
#             cv.imshow("Dialate 4", dial)
#             cv.imshow("Erode 5", erod)
#
#             cv.waitKey(0)
#
#
#
#
#     def area(self):
#         return self.a * self.b
#
#     def printName(self):
#         return self.name
#
#     def sumAreas(o1, o2):
#         print("Sum\t", (round(o1 + o2, 2)))
#
#
# class Circle(Shape):
#     def __init__(self, name, radius):
#         super().__init__(name)
#         self.radius = radius
#         self.name = "circle"
#
#     def circum(self):
#         return 3.14 * (self.radius + self.radius)
#
#     def getArea(self):
#         return 3.14 * self.radius * self.radius
#
#     def printName(self):
#         return self.name
#
#
# # square1 = Square("", 2, 4)
# # print(square1.printName(), "\t", square1.area())
# # circle1 = Circle("", 2)
# # print(circle1.printName(), "\t", circle1.getArea(), "\t", circle1.circum())
# sumAreas(square1.area(), circle1.getArea())