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
IDp='sub1235'
list=[]
list1=[]
list2=[]
list3=[]

def Publisher_registration():
    N3= random.randrange(1000, 5000)
    with open('N3.txt', 'wb') as filehandle:
        pickle.dump(N3, filehandle)
    pickle_file1 = open("VIDp.txt", "rb")
    while True:
        try:
            VIDp = pickle.load(pickle_file1)
        except EOFError:
            break
    pickle_file1.close()
    I=hashlib.md5(VIDp.encode('utf-8'))
    I5=I.hexdigest()
    I6=int(I5,16) ^N3
    return I6
    with open('Pub_regi_send.txt', 'wb') as filehandle:
        for m in list3:
            pickle.dump(m, filehandle)

    list.append(N3)

Publisher_registration()
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Host = socket.gethostbyname(socket.gethostname())
    Port = 5051
    s.connect((Host, Port))
    print(f'Connected to{Host}')
    while True:
        T3=time.time()
        with open('T3.txt', 'wb') as filehandle:
            pickle.dump(T3, filehandle)
        I6=Publisher_registration()
        list3.append(I6)
        list3.append(T3)
        M3 = pickle.dumps(list3)
        s.send(M3)
        receive_SC2 = s.recv(4096)
        I4 = pickle.loads(receive_SC2)
        break
if __name__ == '__main__':
    main()




