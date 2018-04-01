from reader import reader

def main():
    r = reader.Reader("reader/reader.bz2")
    print(r.read())
    r.close()
    r = reader.Reader("reader/reader.gz")
    print(r.read())
    r.close()

if __name__ == '__main__':
    main()
