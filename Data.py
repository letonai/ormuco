import time

''' Item base structur '''
class Data:

    ''' Item  contructor '''
    def __init__(self,data,tzUTC,expirationTime,creationTime=time.time()):
        self.data = data
        self.creationTime = creationTime
        self.expirationTime = expirationTime
        self.tzUTC = tzUTC

    ''' Returns if itens stills valid base on time creation'''    
    def isValid(self):
        return time.time()-self.creationTime<self.expirationTime
    
    ''' invalidade this item instance '''
    def invalidate(self):
        self.expirationTime=0

    def reValidate(self,newExpirationTime):
        self.expirationTime = newExpirationTime
        self.creationTime = time.time()
    
    '''Return seconds since item is invalid '''
    def getExpiredSince(self):

        return time.time()-self.creationTime