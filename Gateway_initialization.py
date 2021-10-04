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
IDs = 'sub1234'
IDp='sub1235'
Lists=[]
list=[]
Listp=[]
curve=registry.get_curve('brainpoolP256r1')
G=curve.g
print(G)
with open('data5.txt', 'wb') as filehandle:
    pickle.dump(G,filehandle)

def compress_point(point):
    return hex(point.x) + hex(point.y % 2)[2:]
privKey_B = secrets.randbelow(curve.field.n)
pubKey_B = privKey_B * G
print('private_Key:',hex(privKey_B))
print('public_key:',compress_point(pubKey_B))
list.append(pubKey_B)
list.append(G)
list.append(curve)
list.append(pubKey_B)
with open('brokerinitialization.txt', 'wb') as filehandle:
    for m in list:
        pickle.dump(m, filehandle)
with open('Broker_secrect_key.txt', 'wb') as filehandle:
    pickle.dump(privKey_B, filehandle)
with open('Broker_public_key.txt', 'wb') as filehandle:
    pickle.dump(pubKey_B, filehandle)
privKey_S = secrets.randbelow(curve.field.n)
pubKey_S = privKey_S * G
Lists.append(privKey_S)
Lists.append(pubKey_S)
with open('subscriberinitialization.txt', 'wb') as filehandle:
    for m in Lists:
        pickle.dump(m, filehandle)
with open('Subscriber_secrect_key.txt', 'wb') as filehandle:
    pickle.dump(privKey_S, filehandle)
with open('Subscriber_public_key.txt', 'wb') as filehandle:
    pickle.dump(pubKey_S, filehandle)
privKey_P = secrets.randbelow(curve.field.n)
pubKey_P = privKey_P * G
Listp.append(privKey_P)
Listp.append(pubKey_P)
with open('publisherinitialization.txt', 'wb') as filehandle:
    for m in Lists:
        pickle.dump(m, filehandle)
with open('Publisher_secrect_key.txt', 'wb') as filehandle:
    pickle.dump(privKey_P, filehandle)
with open('Publisher_public_key.txt', 'wb') as filehandle:
    pickle.dump(pubKey_P, filehandle)
def Subscriber_virtual_identity(ID):
    Ns=random.randrange(1000, 5000)
    Ns1=str(Ns)
    Vs=IDs+Ns1
    Vs1=hashlib.md5(Vs.encode('utf-8'))
    VIDs = Vs1.hexdigest()
    with open('VIDs.txt', 'wb') as filehandle:
        pickle.dump(VIDs, filehandle)
    return VIDs
def Publisher_virtual_identity(ID):
    Np=random.randrange(1000, 5000)
    Np1=str(Np)
    Vp=IDs+Np1
    Vp1=hashlib.md5(Vp.encode('utf-8'))
    VIDp = Vp1.hexdigest()
    with open('VIDp.txt', 'wb') as filehandle:
        pickle.dump(VIDp, filehandle)
    return VIDp
Subscriber_virtual_identity(IDs)
Publisher_virtual_identity(IDp)