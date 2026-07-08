def main():
    result = greet_1("Cedrick")
    print(result) # None
    print(type(result)) # <class 'NoneType'>
    
def greet():
    print("Hello!")

def greet_1(name):
    print(f"Hello {name}")

if __name__ == '__main__':
    main()