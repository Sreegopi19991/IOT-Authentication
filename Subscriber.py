import binascii
import random
import hashlib
import socket
import time

import numpy as np
import pandas as pd
import pickle
import secrets
from tinyec import registry
list=[]
list1=[]
list2=[]
list3=[]
IDs='sub1234'
PW='Sree1234'
curve=registry.get_curve('brainpoolP256r1')
pickle_file = open("data5.txt", "rb")
N=open("N1.txt", "rb")
VID=open("VIDs.txt","rb")
Bs=open("Broker_secrect_key.txt","rb")
Smartcard=open('Smartcard1.txt','rb')
SS=open('Subscriber_secrect_key.txt','rb')
while True:
    try:
        G=pickle.load(pickle_file)
    except EOFError:
        break

    try:
        N1=pickle.load(N)
    except EOFError:
        break

    try:
        VIDS=pickle.load(VID)
    except EOFError:
        break

    try:
        BS=pickle.load(Bs)
    except EOFError:
        break

    try:
        Smartcard1=pickle.load(Smartcard)
    except EOFError:
        break
    try:
        Ss = pickle.load(SS)
    except EOFError:
        break
    try:
        Smartcard1=pickle.load(Smartcard)
    except EOFError:
        break
M=[]
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Host = socket.gethostbyname(socket.gethostname())
    Port = 5051
    s.connect((Host, Port))

    print(f'Connected to{Host}')
    while True:
        def login():
            ID=input("Please enter the ID:")
            Password=input("Please enter password:")
            start = time.time()
            D=VIDS+Password
            H1= hashlib.md5(D.encode('utf-8'))
            H2= H1.hexdigest()
            X1= int(H2,16)^N1
            D1=ID+str(BS)
            H3=hashlib.md5(D1.encode('utf-8'))
            H4=H3.hexdigest()
            X2=X1^int(H4,16)
            if ID==IDs:
                if Password==PW:
                    if X2==Smartcard1:
                        print('Login Successful')
                        I9=N1 * G
                        Ns=str(N1)
                        a_list = [chr(ord(a) ^ ord(b)) for a, b in zip(ID, Ns)]
                        s3 = "".join(a_list)
                        I10=s3
                        D3=int(VIDS,16)+N1
                        H5 = hashlib.md5(str(D3).encode('ASCII'))
                        I11 = H5.hexdigest()
                        M.append(I9)
                        M.append(I10)
                        M.append(I11)
                        send_M=pickle.dumps(M)
                        s.send(send_M)
                        receive_message5 = s.recv(4096)
                        message5 = pickle.loads(receive_message5)
                        a_list1 = [chr(ord(a) ^ ord(b)) for a, b in zip(message5[1], str(Ss))]
                        N3 = "".join(a_list1)
                        a_list2 = [chr(ord(a) ^ ord(b)) for a, b in zip(message5[2], str(Smartcard1))]
                        N2 = "".join(a_list2)
                        PS = open('Subscriber_public_key.txt', 'rb')
                        Ps = pickle.load(PS)
                        I20 = str(N1 * Ps) + str(N2)

                        if I20 == message5[0]:
                            print("Broker is authenticated")
                            S = N1 ^ (int(N2) + int(N3))
                            HK = hashlib.md5(str(S).encode('utf-8'))
                            SK = HK.hexdigest()
                            end = time.time()
                            print(f"Total time for mutual authenticaton is {end - start}")

                            with open('SKB.txt', 'wb') as filehandle:
                                pickle.dump(SK, filehandle)
                else:
                    print('Login failed')

            else:
                print("Login failed")
        break
    login()
if __name__ == '__main__':
    main()




