import math3d as m3d
import socket
import time
import math
import sys
import RG2gripper
import ur

HOST = '192.168.1.10' # The remote host
PORT = 30002 # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket for TCP/IP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Setup socket to be able to reconnect if program is crashed
s.connect((HOST, PORT)) # Connect socket to remote host

ur_state = ur.UR_RobotState(s) # Create ur_state thread object using socket
ur_state.start() # Start the ur_state thread

print(ur_state.get_actual_joint_positions())

# s.send(RG2gripper.openRG2)
# time.sleep(2)
# s.send(RG2gripper.closeRG2)
# time.sleep(2)
# s.send(b'movej([-2.294936005269186, -1.773339410821432, -0.6804609298706055, -1.9333859882750453, 1.486222743988037, 5.052874565124512])'+ b'\n')
# time.sleep(6)
# s.send(b'movej([-1.2883132139789026, -1.794537206689352, -0.6047754287719727, -1.9723202190794886, 1.4289240837097168, 7.04636270204653])'+ b'\n')
def blah['NONE']

def testing(i):
    switcher = {
        0: b'movej(p[-0.02703978368688221, -0.41162562152534876, 0.3339006287927195, 1.6443410877739137, -2.4824781895547496, 0.8022008840211984])'+ b'\n',     # Home
        1: b'movej(p[0.11927293608699337, -0.44964324697824004, 0.07789547669716138, -1.760860569152855, 2.5687295632575915, -0.012967450078887024])'+ b'\n',   # Approach (Gul tape)
        2: b'movej(p[-0.22083692978733743, -0.47504437660265664, 0.07789547669716138, 1.7116764734452912, -2.608166436535716, 0.0687793002035812]'+ b'\n',      # Gul klods aflevering approach
        3: b'movej(p[-0.2223043747395687, -0.4273210328292295, 0.07789547669716138, -1.691223054986082, 2.6459663583454636, -0.02806464578399446]'+ b'\n',      # Rød klods aflevering approach
        4: b'movej(p[-0.22460144592332532, -0.3770031948345641, 0.07789547669716138, -1.6911515816617357, 2.6460350729571416, -0.028088960829898577]'+ b'\n',   # Blå klods aflevering approach
        5: b'movej(p[-0.2246173763400952, -0.33128152957734164, 0.07789547669716138, -1.691150322673192, 2.6460902677637756, -0.02811043675841801]'+ b'\n',     # Grøn klods aflevering approach
        6: b'movej(p[-0.22460908434355267, -0.2850350547556572, 0.07789547669716138, -1.6911234475642323, 2.646071606701752, -0.028114622152454322]'+ b'\n',    # Turkis klods aflevering approach
        7: blah = ur_state.get_tcp_pose()
        8:
        9: RG2gripper.openRG2, #open gripper
        10: RG2gripper.closeRG2, #close gripper
    }
    return switcher.get(i, "Invalid program nummer")

s.send(testing(1))
print(testing(1))

ur_state.stop() # Stop the ur_state thread
s.close() # Close the socket

# if ur_state.is_program_running():
#     time.sleep(0.1)
# else:
#     RG2gripper.closeRG2



###################################
# robot = Robot("192.168.1.26")
# #gripper = OnRobotGripperRG2(robot)
# #time.sleep(0.5)
# # get current pose, transform it and move robot to new pose


# #robot.movej((-1.3917039076434534, -1.481255368595459, -1.365971565246582, -1.7541657886900843, 1.6219735145568848, 6.399825398121969), 0.5, 0.2)
# #robot.movej((-2.1033008734332483, -1.9616223774352015, -1.2292394638061523, -1.088407353763916, 1.4898896217346191, 5.491451263427734), 0.5, 0.2)
# # time.sleep(0.5)


# # if robot.is_program_running():
# #     time.sleep(0.1)
# # else:
# #     gripper.close_gripper()

# robot.close()
# sys.exit()

