
import sys
'''
Simple example to understand context manager
'''

class LoggingContext:
    def __enter__(self):
        LoggingContext.print_message(self, message=None)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

       if exc_type is None:
           LoggingContext.print_message(self, message="normal exit")
       else:
           LoggingContext.print_message(self, message="abnormal exit")
           print("Exception detected:{} {} {}".format(exc_type, exc_val,
                                                      exc_tb))
            

    @staticmethod
    def print_message(self, message):
        print("{}.{}:{}".format(self.__class__.__name__,
                                sys._getframe(1).f_code.co_name,
                                message if message else ""))


def main():
    with LoggingContext() as lc:

        print("working inside logging context")
    print("#"*80)
    try:
        with LoggingContext() as lc2:
            print("working inside logging context")
            raise ValueError("Something went wrong")

    except ValueError:
        print("ValueError occured")

if __name__ == '__main__':
    main()
