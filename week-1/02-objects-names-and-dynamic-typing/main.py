def main():
    x = 10
    y = x
    print(id(x))
    print(id(y))

    a = [1, 2, 3]
    b = a
    b.append(4)
    print(a)
    print(b)

    my_list = ["Python"]
    add_item(my_list)
    print(my_list)

    test = [1,2,3]
    test = test.append(4) # points to None since append returns 'None'
    print(test)

def add_item(items):
    items.append("AI")

def mini_challenge():
    numbers = [1, 2] # binds list to numbers

    alias = numbers # binds alias to the same list object

    numbers.append(3) # mutates the shared list object -> [1, 2, 3]

    alias = [100] # alias was changed to rebind new list object

    print(numbers) # [1, 2, 3]
    print(alias) # [100]

if __name__ == "__main__":
    main()
