#!/usr/bin/env python

'''
Created on July 13, 2016

@author: Shawn Quinn
'''

import subprocess
import sys
import argparse
#
# main program definitiom
#
print("hello Thor user!")
print("executing an echo command")
subprocess.call('echo test text...', shell=True)
    
#
# path to register files
#
leftPath = "/sys/devices/pci0000:00/0000:00:02.0/hx7816_regw_left"
rightPath = "/sys/devices/pci0000:00/0000:00:02.0/hx7816_regw_right"
    
#
# initialize border dimensions to nominal
#
rborder_right = 48
lborder_right = 48
dborder_right = 28
uborder_right = 20
rborder_left = 48
lborder_left = 48
dborder_left = 28
uborder_left = 20
    
#
# parse the command line args
#    arg1 == right shift vertical
#    arg2 == right shift horizontal
#    arg3 == left shift vertical
#    arg4 == left shift horizontal
parser = argparse.ArgumentParser(description='read 4 integer arguments.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

args = parser.parse_args()
rightVert = args.integers[0]
rightHoriz = args.integers[1]
leftVert = args.integers[2]
leftHoriz = args.integers[3]
print "arguments:"
print rightVert
print rightHoriz
print leftVert
print leftHoriz

rborder_right += rightHoriz
lborder_right -= rightHoriz
dborder_right += rightVert
uborder_right -= rightVert
rborder_left += leftHoriz
lborder_left -= leftHoriz
dborder_left += leftVert
uborder_left -= leftVert
            
#
# build up the command strings and print them out
#
# adjust right
#
comm_right_offset = "echo 7b 0f > "
comm_right_offset += rightPath 
comm_rborder_right = "echo 7c "
comm_rborder_right += str(rborder_right)
comm_rborder_right += " > "
comm_rborder_right += rightPath
comm_lborder_right = "echo 7d "
comm_lborder_right += str(lborder_right)
comm_lborder_right += " > "
comm_lborder_right += rightPath
comm_dborder_right = "echo 7c "
comm_dborder_right += str(dborder_right)
comm_dborder_right += " > "
comm_dborder_right += rightPath
comm_uborder_right = "echo 7d "
comm_uborder_right += str(uborder_right)
comm_uborder_right += " > "
comm_uborder_right += rightPath
print(comm_right_offset)
print(comm_rborder_right)
print(comm_lborder_right)
print(comm_dborder_right)
print(comm_uborder_right)

commandSep = "; "
commandMerge = comm_right_offset
for i in range(5) :
    if i == 0 :
        commandMerge += commandSep
    elif i == 1 :
        commandMerge += comm_rborder_right
        commandMerge += commandSep
    elif i == 2 :
        commandMerge += comm_lborder_right
        commandMerge += commandSep
    elif i == 3 :
        commandMerge += comm_dborder_right
        commandMerge += commandSep
    elif i == 4 :
        commandMerge += comm_uborder_right
print(commandMerge)
subprocess.Popen(commandMerge, shell=True)  

#
# adjust left
#
comm_left_offset = "echo 7b 0f > "
comm_left_offset += leftPath 
comm_rborder_left = "echo 7c "
comm_rborder_left += str(rborder_left)
comm_rborder_left += " > "
comm_rborder_left += leftPath
comm_lborder_left = "echo 7d "
comm_lborder_left += str(lborder_left)
comm_lborder_left += " > "
comm_lborder_left += leftPath
comm_dborder_left = "echo 7c "
comm_dborder_left += str(dborder_left)
comm_dborder_left += " > "
comm_dborder_left += leftPath
comm_uborder_left = "echo 7d "
comm_uborder_left += str(uborder_left)
comm_uborder_left += " > "
comm_uborder_left += leftPath
print(comm_left_offset)
print(comm_rborder_left)
print(comm_lborder_left)
print(comm_dborder_left)
print(comm_uborder_left)
          
commandSep = "; "
commandMerge = comm_left_offset
for i in range(5) :
    if i == 0 :
        commandMerge += commandSep
    elif i == 1 :
        commandMerge += comm_rborder_left
        commandMerge += commandSep
    elif i == 2 :
        commandMerge += comm_lborder_left
        commandMerge += commandSep
    elif i == 3 :
        commandMerge += comm_dborder_left
        commandMerge += commandSep
    elif i == 4 :
        commandMerge += comm_uborder_left
print(commandMerge)
subprocess.Popen(commandMerge, shell=True)

