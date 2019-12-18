#!/usr/bin/python3
from lcache import LCACHE
import time
import random
import socket
import sys

id=sys.argv[1]
print(id)
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as con:
    con.connect(('localhost',5000))
    con.sendall(bytes('get,'+sys.argv[1],encoding='UTF-8'))
    data = con.recv(4096)
print(data)
