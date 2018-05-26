import sys
import contextlib
'''
Simple example to understand context manager using contextlib
'''

@contextlib.contextmanager
def logging_context_manager():
    print_message("enter")
    try:
        yield "you are in with block"
        print_message("nomal exit")
    except Exception:
        print_message("abnormal exit")
        print(sys.exc_info())
    


def print_message( message):
        print("{}:{}".format(sys._getframe(1).f_code.co_name,
                                message if message else ""))

def main():
    with logging_context_manager() as lc:

        print("working inside logging context")
    print("#"*80)
    try:
        with logging_context_manager() as lc2:
            print("working inside logging context")
            raise ValueError("Something went wrong")

    except ValueError:
        print("ValueError occured")

if __name__ == '__main__':
    main()
