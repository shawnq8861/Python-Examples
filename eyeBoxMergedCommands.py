#!/usr/bin/env python

'''
Created on May 3, 2016

@author: Shawn Quinn
'''

import subprocess

#
# This class provides C style switch case functionality.
#
class switch(object) :
    def __init__(self, value) :
        self.value = value
        self.fall = False

    def __iter__(self) :
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args) :
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False
#
# main program definitiom
#
def main() :
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
    rborder_left = 48
    lborder_left = 48
    dborder_left = 28
    uborder_left = 20
    rborder_right = 48
    lborder_right = 48
    dborder_right = 28
    uborder_right = 20
    
    #
    # use these variable to keep track of left or right side adjustment
    #
    adjustLeft = False
    adjustRight = False

    #
    # set default selection to ensure while loop executes
    #
    selection = '0'

    while selection != '9' :
        print("Make a Selection:")
        print("    1.  left right")
        print("    2.  left left")
        print("    3.  left down")
        print("    4.  left up")
        print("    5.  right right")
        print("    6.  right left")
        print("    7.  right down")
        print("    8.  right up")
        print("    9.  quit")

        selection = raw_input('Selection:  ')
    
        #
        # get the shift from the user
        #
        for case in switch(selection) :
            if case('1') :   # shift right, decrease right border, left display
                rborder_left -= 1
                lborder_left += 1
                adjustLeft = True
                break
            if case('2') :   # shift left, decrease left border, left display
                lborder_left -= 1
                rborder_left += 1
                adjustLeft = True
                break
            if case('3') :   # shift down, decrease down border, left display
                dborder_left -= 1
                uborder_left += 1
                adjustLeft = True      
                break
            if case('4') :   # shift up, decrease up border, left display
                uborder_left -= 1
                dborder_left += 1
                adjustLeft = True
                break
            if case('5') :   # shift right, decrease right border, right display
                rborder_right -= 1
                lborder_right += 1
                adjustRight = True
                break
            if case('6') :   # shift left, decrease left border, right display
                lborder_right -= 1
                rborder_right += 1
                adjustRight = True
                break
            if case('7') :   # shift down, decrease down border, right display
                dborder_right -= 1
                uborder_right += 1
                adjustRight = True        
                break
            if case('8') :   # shift up, decrease up border, right display
                uborder_right -= 1
                dborder_right += 1
                adjustRight = True
                break
            if case('9') :
                print "good bye!"
                return(0)
                break
            if case() : # default, could also just omit condition or 'if True'
                print "try again!"
                # No need to break here since it is the last case
                
        #
        # build up the command strings and print them out
        #
        if adjustLeft : 
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
            
            adjustLeft = False
            
        if adjustRight :
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
            
            adjustRight = False
        
main()
