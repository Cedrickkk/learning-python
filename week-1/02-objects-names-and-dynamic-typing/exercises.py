def main():
    print('-'*18)
    print('testing exercise 1')
    values = [1, 2, 3]
    add_number_1(values)
    print(values)
    print('-'*18)

    print('-'*18)
    print('testing exercise 2')
    values = [1, 2, 3]
    add_number_2(values)
    print(values)
    print('-'*18)

    print('-'*18)
    print('testing exercise 3')
    values = [1, 2, 3]
    values = add_number_3(values)
    print(values)
    print('-'*18)

def add_number_1(numbers):
    numbers.append(100)

def add_number_2(numbers):
    numbers = [999]
    return numbers

def add_number_3(numbers):
    numbers = [999]
    return numbers


if __name__ == '__main__':
    main()