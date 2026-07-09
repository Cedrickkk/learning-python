def main():
    print(add_item('A'))
    print(add_item('B'))
    print(add_item('C'))
    

def greet():
    print("Hello!")

def greet_1(name):
    print(f"Hello {name}")

def add_item(item, items = None):
    if items is None:
        items = []

    print(id(items))
    
    items.append(item)
    return items

if __name__ == '__main__':
    main()