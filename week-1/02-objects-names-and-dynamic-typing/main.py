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

def add_item(items):
    items.append("AI")

if __name__ == "__main__":
    main()
