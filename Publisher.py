import random
import hashlib
import socket
import time

import numpy as np
import pandas as pd
import pickle
import secrets
from tinyec import registry
import datetime
M4=[]
IDp='sub1235'
pickle_file = open("data5.txt", "rb")
SP=open("Publisher_secrect_key.txt",'rb')
Np=open('N3.txt','rb')
VIDP=open('VIDp.txt','rb')
Smcard2=open('Smartcard2.txt','rb')
PP=open('Publisher_public_key.txt','rb')
BS=open('Broker_secrect_key.txt','rb')
BP=open('Broker_public_key.txt','rb')
M2=[]
T=open('T3.txt','rb')
while True:
    try:
        G=pickle.load(pickle_file)
    except EOFError:
        break
    try:
        Sp=pickle.load(SP)
    except EOFError:
        break
    try:
        N3=pickle.load(Np)
    except EOFError:
        break
    try:
        VIDp=pickle.load(VIDP)
    except EOFError:
        break
    try:
        Smartcard2=pickle.load(Smcard2)
    except EOFError:
        break
    try:
        Pp=pickle.load(PP)
    except EOFError:
        break
    try:
        Bp = pickle.load(BP)
    except EOFError:
        break
    try:
        Bs=pickle.load(BS)
    except EOFError:
        break
    try:
        T3=pickle.load(T)
    except EOFError:
        break
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = socket.gethostbyname(socket.gethostname())
Port = 5051
s.connect((Host, Port))
print(f'Connected to{Host}')
while True:
        print("Sensor connected to gateway")
        receive_message3 = s.recv(4096)
        message3 = pickle.loads(receive_message3)

        N1=message3[1] ^ Sp
        I15=G *N3
        I=Sp *G
        Ip=message3[0]+I
        Ip1=int(VIDp,16) * Ip
        Ns = str(N3)
        a_list = [chr(ord(a) ^ ord(b)) for a, b in zip(IDp, Ns)]
        s3 = "".join(a_list)
        I17=s3
        H1=str(Ip1)+str(T3)+str(N3)
        H2 = hashlib.md5(H1.encode('utf-8'))
        I16= H2.hexdigest()
        M4.append(I15)
        M4.append(I16)
        M4.append(I17)
        send_M4 = pickle.dumps(M4)
        s.send(send_M4)
        receive_message1 = s.recv(10000)
        message1 = pickle.loads(receive_message1)
        N2=message1[1] ^ Smartcard2
        I18=N3*(Pp+Bp)
        if I18==message1[0]:
            print("Broker sucessfully authenticated")
            S=N1 ^(N2+N3)
            HK = hashlib.md5(str(S).encode('utf-8'))
            SK = HK.hexdigest()
            print(SK)
            with open('SKP.txt', 'wb') as filehandle:
                pickle.dump(SK, filehandle)
        break





