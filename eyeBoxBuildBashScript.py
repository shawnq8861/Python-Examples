#!/usr/bin/env python

'''
Created on July 22, 2016

@author: Shawn Quinn
'''

import sys
import argparse
#
# main program definitiom
#
print("hello Thor user!")
    
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
uborder_right = 28
rborder_left = 48
lborder_left = 48
dborder_left = 28
uborder_left = 28
    
#
# parse the command line args
#    arg1 == left shift vertical
#    arg2 == left shift horizontal
#    arg3 == right shift vertical
#    arg4 == right shift horizontal
parser = argparse.ArgumentParser(description='read 4 integer arguments.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

args = parser.parse_args()
leftVert = args.integers[0]
leftHoriz = args.integers[1]
rightVert = args.integers[2]
rightHoriz = args.integers[3]
print "arguments:"
print leftVert
print leftHoriz
print rightVert
print rightHoriz

rborder_right += rightHoriz
rbr_hex_str = hex(rborder_right)
rbr_str_pre, rbr_str_val = rbr_hex_str.split('x')
if rborder_right < 16:
	rbr_str_val = "0" + rbr_str_val

lborder_right -= rightHoriz
lbr_hex_str = hex(lborder_right)
lbr_str_pre, lbr_str_val = lbr_hex_str.split('x')
if lborder_right < 16:
	lbr_str_val = "0" + lbr_str_val

dborder_right += rightVert
dbr_hex_str = hex(dborder_right)
dbr_str_pre, dbr_str_val = dbr_hex_str.split('x')
if dborder_right < 16:
	dbr_str_val = "0" + dbr_str_val

uborder_right -= rightVert
ubr_hex_str = hex(uborder_right)
ubr_str_pre, ubr_str_val = ubr_hex_str.split('x')
if uborder_right < 16:
	ubr_str_val = "0" + ubr_str_val

rborder_left += leftHoriz
rbl_hex_str = hex(rborder_left)
rbl_str_pre, rbl_str_val = rbl_hex_str.split('x')
if rborder_left < 16:
	rbl_str_val = "0" + rbl_str_val

lborder_left -= leftHoriz
lbl_hex_str = hex(lborder_left)
lbl_str_pre, lbl_str_val = lbl_hex_str.split('x')
if lborder_left < 16:
	lbl_str_val = "0" + lbl_str_val

dborder_left += leftVert
dbl_hex_str = hex(dborder_left)
dbl_str_pre, dbl_str_val = dbl_hex_str.split('x')
if dborder_left < 16:
	dbl_str_val = "0" + dbl_str_val

uborder_left -= leftVert
ubl_hex_str = hex(uborder_left)
ubl_str_pre, ubl_str_val = ubl_hex_str.split('x')
if uborder_left < 16:
	ubl_str_val = "0" + ubl_str_val
            
#
# build up the command strings and print them out
#
# adjust right
#
comm_right_offset = "echo 7b 0f > "
comm_right_offset += rightPath 

comm_rborder_right = "echo 7c "
comm_rborder_right += rbr_str_val
comm_rborder_right += " > "
comm_rborder_right += rightPath

comm_lborder_right = "echo 7d "
comm_lborder_right += lbr_str_val
comm_lborder_right += " > "
comm_lborder_right += rightPath

comm_dborder_right = "echo 7c "
comm_dborder_right += dbr_str_val
comm_dborder_right += " > "
comm_dborder_right += rightPath

comm_uborder_right = "echo 7d "
comm_uborder_right += ubr_str_val
comm_uborder_right += " > "
comm_uborder_right += rightPath


print(comm_right_offset)
print(comm_rborder_right)
print(comm_lborder_right)
print(comm_dborder_right)
print(comm_uborder_right)

print('\n')  

#
# adjust left
#
comm_left_offset = "echo 7b 0f > "
comm_left_offset += leftPath
 
comm_rborder_left = "echo 7c "
comm_rborder_left += rbl_str_val
comm_rborder_left += " > "
comm_rborder_left += leftPath

comm_lborder_left = "echo 7d "
comm_lborder_left += lbl_str_val
comm_lborder_left += " > "
comm_lborder_left += leftPath

comm_dborder_left = "echo 7c "
comm_dborder_left += dbl_str_val
comm_dborder_left += " > "
comm_dborder_left += leftPath

comm_uborder_left = "echo 7d "
comm_uborder_left += ubl_str_val
comm_uborder_left += " > "
comm_uborder_left += leftPath

print(comm_left_offset)
print(comm_rborder_left)
print(comm_lborder_left)
print(comm_dborder_left)
print(comm_uborder_left)

#
# open the bash script file and append the text to it
#
script = open("/etc/daqri/eyeBoxAdjust.sh", 'w')
script.write("#!/bin/bash")
script.write('\n')
script.write('\n')
script.write(comm_right_offset)
script.write('\n')
script.write(comm_rborder_right)
script.write('\n')
script.write(comm_lborder_right)
script.write('\n')
script.write(comm_dborder_right)
script.write('\n')
script.write(comm_uborder_right)
script.write('\n')
script.write('\n')
script.write(comm_left_offset)
script.write('\n')
script.write(comm_rborder_left)
script.write('\n')
script.write(comm_lborder_left)
script.write('\n')
script.write(comm_dborder_left)
script.write('\n')
script.write(comm_uborder_left)
script.write('\n')
script.close()

