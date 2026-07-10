def main():
    exercise_1()

    test = ["hello", "john", "cedrick"]
    
    for i in range(5):
        print(i)
    
    print(range(5))
    print(type(range(5)))

    numbers = range(5)

    print(numbers)
    print(list(numbers))

    exercise_2()

def exercise_1():
    numbers = [[1], [2], [3]]

    for number in numbers:
        number.append(100)

    print(numbers)

def exercise_2():
    names = ["Cedrick", "Alice", "Bob"]

    for i, name in enumerate(names):
        print(f"{i + 1}. {name}")

if __name__ == '__main__':
    main()