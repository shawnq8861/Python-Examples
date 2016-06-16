'''
Created on May 2, 2016

@author: Shawn Quinn
'''

import subprocess

def main():
    commandSep = "; "
    command1 = "echo a > testFile.txt"
    command2 = "echo b > testFile.txt"
    command3 = "echo c > testFile.txt"
    command4 = "echo d > testFile.txt"
    command5 = "echo e > testFile.txt"
    for i in range(5) :
        if i == 0 :
            commandMerge  = command1
            commandMerge += commandSep
        elif i == 1 :
            commandMerge += command2
            commandMerge += commandSep
        elif i == 2 :
            commandMerge += command3
            commandMerge += commandSep
        elif i == 3 :
            commandMerge += command4
            commandMerge += commandSep
        elif i == 4 :
            commandMerge += command5
    print(commandMerge)
    subprocess.Popen(commandMerge, shell=True)
    
main()