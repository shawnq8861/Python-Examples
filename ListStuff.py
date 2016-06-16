'''
Created on Mar 31, 2015

@author: shawn
'''

import numpy
from numpy import int16
from numpy import uint32
from numpy import uint16
import sys

myList = [True, False, False, True, True, True, False, True]
print myList
threshold = False
print threshold
for i, x in enumerate(myList):
    if x > threshold:
        myList[i] = False
print myList
numpBoolList = numpy.zeros(7, dtype = bool)
numpIntList = numpy.zeros(7, dtype = int16)
print numpBoolList
print numpIntList
numpIntList[0] = 2
numpIntList[3] = 11
numpIntList[4] = 8
numpIntList[6] = 9
print numpBoolList
print numpIntList
numpBoolList[numpIntList > 0] = True
print numpBoolList
print numpIntList
counter = 0
while True :
    counter = counter + 1
    if counter == 1000000 :
        break
print counter
print 'the end'

bufList = numpy.zeros((4, 6), uint32)
print bufList

intVal = 100
index = 0

for x in xrange(bufList.shape[0]):
    for y in xrange(bufList.shape[1]):
        bufList[x][y] = intVal + index
        index = index + 1
   
print bufList

transList = numpy.transpose(bufList)

print transList

print "row length = " + str(len(transList[:,0]))
