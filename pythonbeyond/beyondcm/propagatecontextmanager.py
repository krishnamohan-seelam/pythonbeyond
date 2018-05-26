import sys
import contextlib
'''
Simple example to understand context manager using contextlib
'''

@contextlib.contextmanager
def propagate_context_manager(name,propagate):
    print_message("enter {}".format(name))
    try:
        yield "you are in with block"
        print_message("{} - normal exit".format(name))
    except Exception:
        print_message("{} - abnormal exit".format(name))
        print(name,"received an exception")
        if propagate:
            raise
    

def print_message( message):
        print("{}:{}".format(sys._getframe(1).f_code.co_name,
                                message if message else ""))

def main():
    with propagate_context_manager('outer',True) ,propagate_context_manager('inner',False) :
         raise ValueError("Something went wrong")

if __name__ == '__main__':
    main()
