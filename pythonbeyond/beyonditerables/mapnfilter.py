'''
mapnfilter
To demonstrate map usage on single input sequence and multiple input sequence
also uses lambda,list comprehensions
'''


def print_output(message, contents):
    if message:
        print(message)
    if contents:
        print(contents)


def main():
    fruits = ['apple', 'banana', 'cherry', 'orange', 'strawberry']
    print_output("before applying map function on fruits", fruits)
    fruits = list(map(str.upper, fruits))
    print_output("after applying map function on fruits", fruits)
    even = [x for x in range(51) if x % 2 == 0]
    print_output("even numbers:", even)
    odd = [x for x in range(51) if x % 2 != 0]
    print_output("odd numbers:", odd)
    sum_of_numbers = list(map(lambda x, y: x + y, list(even), list(odd)))
    print_output("sum_of_numbers using multiple input sequence",
                 sum_of_numbers)
    print_output("observe even numbers and odd  number sizes are different\
 but map terminates on exhaust of either of input sequences", None)
    print_output("filter example:", None)
    seven_heaven = list(filter(lambda x: (x % 7==0),sum_of_numbers))
    print_output("All seven heavens", seven_heaven)

if __name__ == '__main__':
    main()
