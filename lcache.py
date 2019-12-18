import string
import random
import uuid
import time
import threading
import socket
import select
from Data import Data

''''Could not finish this chalange'''

class LCACHE:
    ''' Classa contructor'''
    def __init__(self,maxCacheSize, defaultExpirationTime,serverAddress=None,serverPort=None):
        # Number of elements on cache
        self.maxCacheSize = maxCacheSize
        # default Expiration Time for caches
        self.defaultExpirationTime = defaultExpirationTime
        self.cache = dict()
        self.serverAddress = serverAddress
        self.serverPort = serverPort
        '''' if no address to connect is passed, start as client '''
        if self.serverAddress == None:
            self.startServer()
        ''' Starts a cache validation thread '''
        monitor = threading.Thread(target=self.validCacheMonitor,args=[])
        monitor.start()

    ''' Start the server '''
    def startServer(self):
        server = threading.Thread(target=self.server,args=[])
        server.start()                        
                
     '''' Server code '''    
    def server(self):
        HOST = ''
        PORT = 5000
        tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp.bind((HOST,PORT))
        tcp.listen(1)
    
        while True:
            con,client = tcp.accept()
            print("Connected %s" % str(client))
            while True:
                requestData = con.recv(4096)
                print(len(requestData))
                if len(requestData) >0:
                    print(str(requestData))
                    if "get" in str(requestData):
                        key=str(str(requestData).split(",")[1]).replace("'","")
                        print("Comando aceito %s-" % key)
                        data=self.cache.get(key)
                        print(data)
                        if data != None:
                            con.send(bytes(str(self.cache.get(key)),encoding='UTF-8'))
                else:
                    con.close()
                    break               

    ''' Return data for the given key '''                
    def get(self,key):
        try:
            if self.cache[key].isValid():
                return self.cache[key]
            else:
                return None
        except KeyError:
            return None
    ''' Creates a new item in cache  and returns it's id'''
    def set(self,value):
        itemId=self.newItemId()
        data = Data(value,0,self.defaultExpirationTime)
        self.cache[str(itemId)] = data
        print(itemId)
        return itemId

    ''' invalidate '''
    def invalidateItem(self,key):
        cache[key].invalidate()


    ''' Generates a random item id to be used '''
    def newItemId(self,lenght=16):
        return ('%06x' % random.randrange(16**lenght)).upper()
    ''' Removes an item from cache '''
    def purgeItem(self,key):
        cache.pop(key)

    ''' Routine to check for expired items '''
    def validCacheMonitor(self):
        while True:
            time.sleep(1)
            try:
                for item in self.cache.keys():
                    if self.cache[item].isValid():
                        print(item+":"+str(self.cache[item].isValid())+":"+str(self.cache[item].expirationTime))
                    ''' items older then 500 seconds are purged '''
                    elif not self.cache[item].isValid() and self.cache[item].getExpiredSince()>500:
                        purgeItem(item)
            except:
                continue        