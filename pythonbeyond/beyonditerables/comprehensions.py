'''
comprehensions
To demonstrate list comprehensions,set comprehensions
'''


def main():
    even_list = [i for i in range(0, 101) if (i % 2) == 0]
    even_set = {i for i in range(0, 101) if (i % 2) == 0}
    print("even list")
    print(even_list)
    print("even set")
    print(even_set)
    cartesian = [(x, y) for x in range(5)
                 for y in range(3)]
    print("cartesian")
    print(cartesian)
    values = [(x / x - y)
              for x in range(10)
              if x > 5
              for y in range(10)
              if (x - y) != 0]
    print("values:")
    print(values)
    triangulation = [(x, y) for x in range(10) for y in range(x)]
    print("triangulation:")
    print(triangulation)


if __name__ == '__main__':
    main()
