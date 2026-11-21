'''1. Write a Python program that attempts to dynamically import a module at runtime.
The program should only import the module if it actually exists; otherwise, it
should print "Module does not exist".'''

#'''
import importlib

m = input("Enter module name: ")    #math (exist), #abcd (doesn't exist)

try:
    module = importlib.import_module(m)
    print("Module imported")
except ModuleNotFoundError:
    print("Module doesn't exist")
#'''

