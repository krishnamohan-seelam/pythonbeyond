
def sortby_last_letter(strings):
    def last_letter(s):
        return s[-1]
    return sorted(strings,key=last_letter)

def outer(y):
    x=10
    def inner(y):
        return x+y
    return inner(y)


if __name__ == '__main__':
    fruits =['apple','banana','cherry','jack fruit','manago']
    print(sortby_last_letter(fruits))
    print("using outer variable  by local function")
    print(outer(10))

