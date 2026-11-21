'''3. Create two Python modules that import each other. Run the program
to observe what happens with circular imports. Then think of different ways
to prevent a circular-import crash. '''

'''
import ModuleB3

def displayA():
    print("ModuleA")
ModuleB3.displayB()
'''

#Above code will raise AttributeError: ModuleB3 has no attribute displayB
#To overcome that error we move this inside a function.


def displayA():
    print("ModuleA")

def callB():
    import ModuleB3
    ModuleB3.displayB()