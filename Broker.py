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
Adr=[]
M1=[]
M2=[]
M4=[]
M5=[]
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host= socket.gethostbyname(socket.gethostname())
Port=5051
try:
    s.bind((Host, Port))
except socket.error as e:
    print(str(e))
s.listen()
clientsocket,adress=s.accept()
IDs = 'sub1234'
IDp='sub1235'
pickle_file = open("data5.txt", "rb")
VID=open("VIDs.txt","rb")
Nb=open("N2.txt","rb")
SP=open('Publisher_secrect_key.txt','rb')
VIDP=open('VIDp.txt','rb')
T=open('T3.txt','rb')
Bs=open("Broker_secrect_key.txt","rb")
Smcard2=open('Smartcard2.txt','rb')
SS=open('Subscriber_secrect_key.txt','rb')
Smcard1=open('Smartcard1.txt','rb')
while True:
    try:
        G=pickle.load(pickle_file)
    except EOFError:
        break
    try:
        VIDS=pickle.load(VID)
    except EOFError:
        break
    try:
        N2=pickle.load(Nb)
    except EOFError:
        break
    try:
        Sp=pickle.load(SP)
    except EOFError:
        break
    try:
        VIDp=pickle.load(VIDP)
    except EOFError:
        break

    try:
        BS=pickle.load(Bs)
    except EOFError:
        break
    try:
        T3=pickle.load(T)
    except EOFError:
        break
    try:
        Smartcard2=pickle.load(Smcard2)
    except EOFError:
        break
    try:
        Smartcard1=pickle.load(Smcard1)
    except EOFError:
        break
    try:
        Ss = pickle.load(SS)
    except EOFError:
        break


with clientsocket:

    print(f'new device {adress} is connected')
    clientsocket2,adress=s.accept()
    with clientsocket2:
        print(f'new device {adress} is connected')
        while True:
            receive_message1 = clientsocket.recv(4096)
            message1 = pickle.loads(receive_message1)
            N=[chr(ord(a) ^ ord(b)) for a, b in zip(IDs, message1[1])]
            N1="".join(N)
            N1=int (N1)
            D3 = int(VIDS, 16) + N1
            H5 = hashlib.md5(str(D3).encode('ASCII'))
            I11 = H5.hexdigest()
            if I11==message1[2]:
                print('Subscriber is athenticated')
                I12=G * N2
                I13=Sp *G
                I14=Sp ^ N1
                M2.append(I12)
                M2.append(I14)

                send_M2 = pickle.dumps(M2)
                clientsocket2.send(send_M2)

                receive_message3 = clientsocket2.recv(4096)
                message3 = pickle.loads(receive_message3)

                a_list = [chr(ord(a) ^ ord(b)) for a, b in zip(IDp,message3[2])]
                N3 = "".join(a_list)
                P1=I13+I12
                P2=int(VIDp,16)*P1
                P3=str(P2)+str(T3)+str(N3)
                P4 = hashlib.md5(P3.encode('utf-8'))
                I16 = P4.hexdigest()
                print(I16)
                if I16==message3[1]:
                    print("Publisher is authenticated")
                    I18=message3[0]*(Sp+BS)
                    I19=N2 ^ Smartcard2
                    M4.append(I18)
                    M4.append(I19)
                    send_M4 = pickle.dumps(M4)
                    clientsocket2.send(send_M4)
                    X1=N1*G*Ss
                    C20=str(X1)+str(N2)
                    a_list1 = [chr(ord(a) ^ ord(b)) for a, b in zip(str(N3), str(Ss))]
                    C21 = "".join(a_list1)
                    a_list2 = [chr(ord(a) ^ ord(b)) for a, b in zip(str(N2), str(Smartcard1))]
                    C22 = "".join(a_list2)

                    M5.append(C20)
                    M5.append(C21)
                    M5.append(C22)
                    send_M5 = pickle.dumps(M5)

                    clientsocket.send(send_M5)
                    S = N1 ^ (N2 + int(N3))

                    HK = hashlib.md5(str(S).encode('utf-8'))
                    SK = HK.hexdigest()
                    print(SK)

                    with open('SKB.txt', 'wb') as filehandle:
                        pickle.dump(SK, filehandle)



            else:
                print('Authentication failed')

            break





