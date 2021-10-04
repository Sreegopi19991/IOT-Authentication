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
while True:
    try:
        G=pickle.load(pickle_file)
    except EOFError:
        break
pickle_file.close()
print(G)

def Subscriber_registration():
    N1 = random.randrange(1000, 5000)

    pickle_file1 = open("VIDs.txt", "rb")
    while True:
        try:
            VIDs = pickle.load(pickle_file1)
        except EOFError:
            break
    pickle_file1.close()

    M=VIDs+PW
    I=hashlib.md5(M.encode('utf-8'))
    I1=I.hexdigest()
    I2=int(I1,16) ^N1
    list2.append(I2)
    list2.append(VIDs)
    list1.append(N1)
    with open('N1.txt', 'wb') as filehandle:
        pickle.dump(N1, filehandle)
    return I2
Subscriber_registration()
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Host = socket.gethostbyname(socket.gethostname())
    Port = 5051
    s.connect((Host, Port))
    print(f'Connected to{Host}')
    while True:
     I2 = Subscriber_registration()
     T1=time.time()
     list3.append(I2)
     list3.append(T1)
     M1=pickle.dumps(list3)
     print(M1)
     s.send(M1)
     receive_SC1 = s.recv(4096)
     I4 = pickle.loads(receive_SC1)

     break
if __name__ == '__main__':
    main()




