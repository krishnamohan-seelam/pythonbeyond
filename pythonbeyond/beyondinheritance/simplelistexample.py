from simplelist import SimpleList, SortedList, IntList,SortedIntList


def main():
    sl = SimpleList([1, 2, 34, 67])
    print(sl)
    sl.add(100)
    print(sl)
    sortl = SortedList([45, 23, 67, 33, 20, 0])
    print(sortl)
    sortl.add(100)
    intl = IntList([0, 1, 2, 3, 4])
    print(intl)
    sortil = SortedIntList([45, 23, 67, 33, 20, 0])
    print(sortil)
    try:
        intl.add('x')
    except ValueError as ve:
        print(ve)


if __name__ == '__main__':
    main()
