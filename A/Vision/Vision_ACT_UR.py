import ur
import socket
import math
import time
import numpy as np
import urrobot

import RG2_Boilerx2 #Fjern v. simulering!

HOST = '192.168.1.10' # The remote host
PORT = 30002 # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket for TCP/IP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Setup socket to be able to reconnect if program is crashed
s.connect((HOST, PORT)) # Connect socket to remote host

ur_state = ur.UR_RobotState(s) # Create ur_state thread object using socket
ur_state.start() # Start the ur_state thread

urr = urrobot.URRobot(s)


s.send(b'movel(pose_trans(p[-58.87, -552.10, 51.55, 1.633, -2.590, 0.257],p[-60.35, 99.75, -0.32, 1.715, -2.632, -0.000]),\n')


# s.send(b'movej(p[0.11927293608699337, -0.44964324697824004, 0.07789547669716138, -1.760860569152855, 2.5687295632575915, -0.012967450078887024]), p[res_pose]'+ b'\n') # Gul tape approach TCP

# URRobot._wait_for_move('[0.11927293608699337, -0.44964324697824004, 0.07789547669716138, -1.760860569152855, 2.5687295632575915, -0.012967450078887024]') #target = 'p[0.11927293608699337, -0.44964324697824004, 0.07789547669716138, -1.760860569152855, 2.5687295632575915, -0.012967450078887024]', threshold= 0.5



# s.send(RG2_Boilerx2.openRG2)
# time.sleep(5)

# s.send(b'movel(p[0.11996803611715218, -0.4493667428662896, 0.03232317781105842, -1.7608991870696928, 2.568698525414194, -0.012693174188054119])'+ b'\n') # Gul tape TCP
# time.sleep(5)

# s.send(RG2_Boilerx2.closeRG2)
# time.sleep(5)

# s.send(b'movel(p[0.11927293608699337, -0.44964324697824004, 0.07789547669716138, -1.760860569152855, 2.5687295632575915, -0.012967450078887024])'+ b'\n') # Gul tape approach TCP
# time.sleep(5)

# s.send(b'movej(p[-0.22083692978733743, -0.47504437660265664, 0.07789547669716138, 1.7116764734452912, -2.608166436535716, 0.0687793002035812])'+ b'\n') # Gul aflevering approach TCP
# time.sleep(5)

# s.send(b'movel(p[-0.22443930620307248, -0.47390900282055476, 0.05852415725442153, 1.7046177888286387, -2.6107060144093945, 0.0004146157460056376])'+ b'\n') # Gul aflevering TCP
# time.sleep(5)

# s.send(RG2_Boilerx2.openRG2)
# time.sleep(5)

# s.send(b'movel(p[-0.22083692978733743, -0.47504437660265664, 0.07789547669716138, 1.7116764734452912, -2.608166436535716, 0.0687793002035812])'+ b'\n') # Gul aflevering approach TCP
# time.sleep(5)



rad = ur_state.get_actual_joint_positions()
print("Radianer: ", rad, "\n")
tcp = ur_state.get_tcp_pose()
print("TCP Pose: ", tcp)

# for x in range(6):
    # grad = ((rad[x]*180)/math.pi)
        
    # print("Grader joint", x, ":", grad, "\n")
    # time.sleep(1)

# s.send(b'movej([-3.1535757223712366, -2.2041880093016566, -0.7011871337890625, -1.4965036672404786, 1.4888596534729004, 4.5586957931518555])'+ b'\n')
# time.sleep(5)



s.send(RG2_Boilerx2.openRG2)
time.sleep(5)

s.send(RG2_Boilerx2.closeRG2)
time.sleep(5)

# rad = ur_state.get_actual_joint_positions()
# print("Radianer: ", rad, "\n")

# for x in range(6):
#     grad = ((rad[x]*180)/math.pi)
        
        
#     print("Grader joint", x, ":", grad, "\n")
#     time.sleep(1)




ur_state.stop()
s.close()


