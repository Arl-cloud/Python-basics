#Modules

import time

#while True:
#    print("jonas stinkt")
#    time.sleep(10)
#loop beenden mit control + c

#Builtin Modules
#e.g. dir(dict)

#type in active shell
import sys
sys.builtin_module_names

#import time
#dir(time)
#help(time.sleep)

time.sleep(3) #sleep "sleeps" the script /delays execution for a given number of seconds

#Standard Python Modules

import os
#to find out where this module is located:
sys.prefix
#/Library/Frameworks/Python.framework/Versions/3.8
#while True:
#    with open("plants.txt") as file:
#        print (file.read())
#        time.sleep(10)
    
#enter in terminal after error occurs (file not found):
#"open /Library/Frameworks/Python.framework/Versions/3.8"
#open "lib" folder, then "Python 3.8"
#the python files there are all standard python files
#double-click os
os.path.exists("/Users/arleenlindenmeyer/Desktop/Python/plants.txt")
#output: False, bc file is not in the Python folder
os.path.exists("/Users/arleenlindenmeyer/Desktop/Python/fruits.txt")
#output: True, bc file can be found under this path

import os #not builtin, but a script copied in a python file

#while True:
#    if os.path.exists("/Users/arleenlindenmeyer/Desktop/Python/fruits.txt"):
#        with open("fruits.txt") as file:
#            print (file.read())
#    else:
#        print("File does not exist.")
#    time.sleep(10) #outside of if condition, if you want this executed regardless of condition     

#temps_today file: every column has data (st1, st2)
#print out average value every 10 seconds

#third party library (pandas): pip can be used to install other 3rd party libraries
#pip3 install pandas
import pandas #package = several modules

while True:
    if os.path.exists("/Users/arleenlindenmeyer/Desktop/Python/temps_today.csv"):
        data = pandas.read_csv("/Users/arleenlindenmeyer/Desktop/Python/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("file does not exist.")
    time.sleep(10)
#output: prints out mean of st1 column every 10 seconds