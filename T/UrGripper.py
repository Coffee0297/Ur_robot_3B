import ur
import socket
import Gripper
# Made by TLM
host = '10.0.0.134'  # the remote host
port = 30002 # the same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket for tcp/ip
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # setup socket to be able to reconnect if program is crashed
s.connect((host, port))  # connect socket to remote host

ur_state = ur.UR_RobotState(s)  # create ur_state thread object using socket
ur_state.start()  # start the ur_state thread


def testing(i):
    switcher = {
        0: b'movej(p[-0.02703978368688221, -0.41162562152534876, 0.3339006287927195, 1.6443410877739137, -2.4824781895547496, 0.8022008840211984])'+ b'\n', # Home
        3: b'movej(p[-0.2223043747395687, -0.4273210328292295, 0.07789547669716138, -1.691223054986082, 2.6459663583454636, -0.02806464578399446]'+ b'\n', # Rød klods aflevering approach
        4: b'movej(p[-0.22460144592332532, -0.3770031948345641, 0.07789547669716138, -1.6911515816617357, 2.6460350729571416, -0.028088960829898577]'+ b'\n', # Blå klods aflevering approach
        5: b'movej(p[-0.2246173763400952, -0.33128152957734164, 0.07789547669716138, -1.691150322673192, 2.6460902677637756, -0.02811043675841801]'+ b'\n', # Grøn klods aflevering approach
        7: Gripper.gopen, #open gripper
        8: Gripper.gclose, #close gripper
    }
    return switcher.get(i, "Invalid program nummer")

s.send(testing(0))
print(testing(0))

ur_state.stop() # stop the ur_state thread
s.close() # close the socket
