
'''
Simple example to demonstrate importing.
This will help us in understanding of how modules are imported.This will explain
 how  sys.path searches for modules that defined python program.
'''
import sys
def main():
    print("trying to import helper module")
    from helper import helper
    helper.print_details()
    sys.path.append(r'F:\projects\pyprojects\extrahelper')
    from extrahelper import extrahelper
    extrahelper.print_extrahelper()
    print("Try to comment sys.path.append and execute the program")
 

if __name__ == '__main__':
    main()