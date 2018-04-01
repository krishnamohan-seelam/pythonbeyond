from reader import reader

def main():
    r = reader.Reader("reader/__init__.py")
    line =r.read()
    print(line)
    print("if the above line  was not declared in __init__.py")
    print("we require this :from reader import reader")
    print("To access Reader :r = reader.Reader('reader/__init__.py')")
    print("Try removing {0} in __init__.py from reader directory".format(line))
    r.close()

if __name__ == '__main__':
    main()
