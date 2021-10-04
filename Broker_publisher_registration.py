import pandas as pd
import random
import hashlib
import socket
import numpy as np
import pandas as pd
import pickle
import threading
import secrets
import tinyec
from tinyec import registry
import time
list5=[]
list6=[]
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host= socket.gethostbyname(socket.gethostname())
Port=5051
try:
    s.bind((Host, Port))
except socket.error as e:
    print(str(e))
IDs = 'sub1234'
IDp='sub1235'
curve = registry.get_curve('brainpoolP256r1')
pickle_file = open("data5.txt", "rb")
pickle_file1 = open("Broker_secrect_key.txt", "rb")
while True:
    try:
        G = pickle.load(pickle_file)
    except EOFError:
        break
    try:
        privKey_B = pickle.load(pickle_file1)
    except EOFError:
        break
pickle_file.close()
pickle_file1.close()
def Broker_1(clientsocket, adress):
    print(f'new device {adress} is connected')
    while True:

        T2=time.time()
        R_M3=clientsocket.recv(1024)
        M3=pickle.loads(R_M3)
        T3=M3[1]
        T=T2-T3
        print(T)
        if T<=0.100:
            B1=str(privKey_B)
            S1=IDp+B1
            B2=hashlib.md5(S1.encode('utf-8'))
            I7=B2.hexdigest()
            I8= int(I7,16) ^ M3[0]
            with open('Smartcard2.txt', 'wb') as filehandle:
                pickle.dump(I8, filehandle)
            M4 = pickle.dumps(I8)


            clientsocket.send(M4)
        break



def start():
    s.listen(5)
    while True:
        clientsocket, adress = s.accept()
        thread=threading.Thread(target=Broker_1,args=(clientsocket,adress))
        thread.start()
        print(f'[active connections{threading.active_count()-1}')
        break
start()





