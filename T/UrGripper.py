import time
import math
import sys
import ur
import socket
import test

host = '192.168.1.10' # the remote host
port = 30002 # the same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket for tcp/ip
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # setup socket to be able to reconnect if program is crashed
s.connect((host, port)) # connect socket to remote host

ur_state = ur.UR_RobotState(s) # create ur_state thread object using socket
ur_state.start() # start the ur_state thread




def testing(i):
    switcher = {
        0: b'movej(p[-0.02703978368688221, -0.41162562152534876, 0.3339006287927195, 1.6443410877739137, -2.4824781895547496, 0.8022008840211984])'+ b'\n', # Home
        1: b'movel(pose_trans(p[-0.05868045378166816, -0.5515318145847172, 0.05261378708660652, 2.4527356468783705, 1.708290331580861, 0.01],p[0.1,0.0,-0,0,0 , 0]), a=0.2, v=0.3, t=0)'+ b'\n', # Approach (Gul tape)
        2: b'movej(p[-0.22083692978733743, -0.47504437660265664, 0.07789547669716138, 1.7116764734452912, -2.608166436535716, 0.0687793002035812]'+ b'\n', # Gul klods aflevering approach
        3: b'movej(p[-0.2223043747395687, -0.4273210328292295, 0.07789547669716138, -1.691223054986082, 2.6459663583454636, -0.02806464578399446]'+ b'\n', # Rød klods aflevering approach
        4: b'movej(p[-0.22460144592332532, -0.3770031948345641, 0.07789547669716138, -1.6911515816617357, 2.6460350729571416, -0.028088960829898577]'+ b'\n', # Blå klods aflevering approach
        5: b'movej(p[-0.2246173763400952, -0.33128152957734164, 0.07789547669716138, -1.691150322673192, 2.6460902677637756, -0.02811043675841801]'+ b'\n', # Grøn klods aflevering approach
        6: b'movej(p[-0.22460908434355267, -0.2850350547556572, 0.07789547669716138, -1.6911234475642323, 2.646071606701752, -0.028114622152454322]'+ b'\n', # Turkis klods aflevering approach
        7: test.gopen, #open gripper
        8: test.gclose, #close gripper
    }
    return switcher.get(i, "Invalid program nummer")

s.send(testing(1))
print(testing(1))

ur_state.stop() # stop the ur_state thread
s.close() # close the socket
