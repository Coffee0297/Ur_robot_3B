import ur
import cv2 as cv
import socket
import Gripper
import Program
import time

# Made by TLM

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket for tcp/ip
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                 1)  # setup socket to be able to reconnect if program is crashed
    s.connect((host, port))  # connect socket to remote host

    ur_state = ur.UR_RobotState(s)  # create ur_state thread object using socket
    ur_state.start()  # start the ur_state thread
    return s, ur_state


def return_klods():
    rad, x, y, fave = Program.main()
    Ys = str(y[-1] + y_workspace_offset)
    Yb = bytes(Ys, encoding='utf8')

    Xs = str(x[-1] + x_workspace_offset)
    Xb = bytes(Xs, encoding='utf8')

    Rs = str(rad[0][-1])
    Rb = bytes(Rs, encoding='utf8')

    klods = (Xb + b"," + Yb)
    rotation = (Rb + b"]")
    return klods, rotation, fave


def moves(i):
    switcher = {
        0: b'movej(p[0.4254, 0.709, 0.750, 1.99, -3.0, -2.351])' + b'\n',  # Home
        1: b'movej(p[' + klods + b", 0.0778, 2.897, -1.32," + rotation + b')' + b'\n',
        # Go to pos that the vision program says
        2: b'movej(p[' + klods + b", 0.020, 2.897, -1.32," + rotation + b')' + b'\n',
        # Go to pos that the vision program says - 50mm
        3: b'movej(p[0.2223, -0.4273, 0.0778, -1.6912, 2.6459, -0.0280])' + b'\n',  # Rød klods aflevering approach
        4: b'movej(p[0.2223, -0.4273, 0.020, -1.6912, 2.6459, -0.0280])' + b'\n',  # Rød klods aflevering
        5: b'movej(p[0.2246, -0.3770, 0.0778, -1.6911, 2.6460, -0.02808])' + b'\n',  # Blå klods aflevering approach
        6: b'movej(p[0.2246, -0.3770, 0.020, -1.6911, 2.6460, -0.02808])' + b'\n',  # Blå klods aflevering
        7: b'movej(p[0.2246, -0.3312, 0.0778, -1.6911, 2.6460, -0.0281])' + b'\n',  # Grøn klods aflevering approach
        8: b'movej(p[0.2246, -0.3312, 0.020, -1.6911, 2.6460, -0.0281])' + b'\n',  # Grøn klods aflevering
        9: b"movej(p[0.2450, -0.2909, 0.0778, -0.9353, -2.9870, -0.0248])" + b'\n',  # Gul klods aflevering approach
        10: b"movej(p[0.2450, -0.2909, 0.020, -0.9353, -2.9870, -0.0248])" + b'\n',  # Gul klods aflevering
        11: Gripper.gopen,  # open gripper
        12: Gripper.gclose,  # close gripper
    }
    return switcher.get(i, "Invalid program nummer")


def wait_till_done():
    time.sleep(0.3)
    while True:
        if ur.UR_RobotState.is_program_running(ur_states) == False:
            print(ur.UR_RobotState.is_program_running(ur_states))
            print("Move done")
            break


host = '10.0.0.134'  # the remote host
port = 30002  # the same port as used by the server
x_workspace_offset = 0.300  # Offset form robot base to the 0,0 on the paper in M
y_workspace_offset = 0.300  # Offset form robot base to the 0,0 on the paper in M

s, ur_states = connect()
klods, rotation, farve = return_klods()
print("Type Run to start the robot")
k = input()
print(k)
if k == str("run"):
    while True:
        if ur.UR_RobotState.is_real_robot_enabled(ur_states):  # wait for SPACE key to Run
            s.send(moves(0))
            wait_till_done()
            klods, rotation, farve = return_klods()
            s.send(moves(1))
            wait_till_done()

            # s.send(moves(11))   # open gripper don't work in sim
            # wait_till_done()
            s.send(moves(2))
            wait_till_done()

            # s.send(moves(12))   # close gripper don't work in sim
            # wait_till_done()
            s.send(moves(1))
            wait_till_done()

            if farve == 1:
                print("Red")
                s.send(moves(3))
                wait_till_done()

                s.send(moves(4))
                wait_till_done()

                # s.send(moves(11))   # open gripper don't work in sim
                # wait_till_done()
                s.send(moves(3))
                wait_till_done()

            if farve == 2:
                print("Green")
                s.send(moves(7))
                wait_till_done()

                s.send(moves(8))
                wait_till_done()

                # s.send(moves(11))   # open gripper don't work in sim
                # wait_till_done()
                s.send(moves(7))
                wait_till_done()

            if farve == 3:
                print("Blue")
                s.send(moves(5))
                wait_till_done()

                s.send(moves(6))
                wait_till_done()

                # s.send(moves(11))   # open gripper don't work in sim
                # wait_till_done()
                s.send(moves(5))
                wait_till_done()

            if farve == 4:
                print("yellow")
                s.send(moves(9))
                wait_till_done()

                s.send(moves(10))
                wait_till_done()

                # s.send(moves(11))   # open gripper don't work in sim
                # wait_till_done()
                s.send(moves(9))
                wait_till_done()

        else:
            print("Robot not ready")

ur_states.stop()  # stop the ur_state thread
time.sleep(0.3)
s.close()  # close the socket
