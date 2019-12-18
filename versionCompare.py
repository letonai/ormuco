#!/usr/bin/python3
import sys
import re

'''Compare two versions and return the newer one'''
def VersionCheck(version1,version2):
    if len(re.sub(r'[0-9.]+', '',version1+version2))>0:
        print("Entred parameter is not valid")
        return 1
    v1 = float("0."+version1.replace(".",""))
    v2 = float("0."+version2.replace(".",""))
    if v1>v2:
        print("Version %s is newer than %s" %(version1,version2))
    if v1==v2:
        print("Version %s is the same as %s" %(version1,version2))
    if v1<v2:
        print("Version %s is newer than %s" %(version2,version1))
        return 0

VersionCheck(sys.argv[1],sys.argv[2])

''''Test Cases
VersionCheck(1.0,1.0)
VersionCheck(1.0,2.0)
VersionCheck(2.0,2.1)
VersionCheck(1.0,1.000000)
VersionCheck(1.00000001,1.0)
VersionCheck(1.0,1.0.0.0.0.0.0)
VersionCheck(1.0,1.0a)
VersionCheck(1.0,0.0.1.1.11)
VersionCheck(1.0.2,1.0)
'''