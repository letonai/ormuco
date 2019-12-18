#!/usr/bin/python3
from lcache import LCACHE
import time
import random


cache = LCACHE(10000,50)
print(cache.maxCacheSize)
print(cache.cache)
print(cache.defaultExpirationTime)
print(len(cache.cache))
#cache.cache[1]=None
bt=time.time()
f = open("document.pdf","r",encoding="ISO-8859-1")
file = f.read(-1)
fid= cache.set(file)
print(time.time()-bt)
id=None
for _ in range(10): 
    time.sleep(.2)
    d="Teste de item novo "
    id=cache.set(d)
print("PRONTO "+id)
time.sleep(5)





