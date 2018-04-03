'''
The below example demonstrates how decorators can be implemented using classes,
instances ,how  to use multiple decorators
'''


class CallCount:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


class Tracer:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print("From {0},calling function {1}".format(
                      self.__class__.__name__,
                      f.__name__))
            return f(*args, **kwargs)
        return wrap


tracer = Tracer()


@CallCount
@tracer
def hello(name):
    print("Hello {0}".format(name))


if __name__ == '__main__':
    hello("Krishna")
    hello("Swathi")
    hello("Geetha")
    print("Number of times function hello called :{0}".format(hello.count))
