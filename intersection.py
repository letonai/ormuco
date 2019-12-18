#!/usr/bin/python3
import sys
import re

'''Receives 4 values and check if lines intersects, returns true or false'''
def CheckIntersection(x1,y1,x2,y2):

    if (x1 >= x2 and x1 <= y2 or x2 >= x1 and x2 <= y1 ):
        return True
    else:
	    return False

if CheckIntersection(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]):
    print("intersect")
    return True
else:
    print("don't intersect")
    return False