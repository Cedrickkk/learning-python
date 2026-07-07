def main():
    challenge()

def example_1():
    a = [1, 2, 3]
    b = a.copy()
    print(a is b)
    print(a == b)

def example_2(): 
    a = [[1], [2]]
    b = a.copy()
    b.append([3])
    print(a)
    print(b)

def example_3(): 
    a = [[1], [2]]
    b = a.copy() # copy the outer list but the inner list values are shared
    b[0].append(99) # modifies the inner list values
    print(a)
    print(b)

def example_4():
    conversation = [
        { "role": "user", "content": "Hello" }, 
        { "role": "assistant", "content": "Hi!" }
    ]

    working = conversation.copy()

    working[0]["content"] = "Changed"

    print(working)
    print(conversation)

    print(working is conversation)

def challenge():
    person = {
        "name": "Cedrick",
        "skills": ["Java", "Python"]
    }

    copy_person = person.copy() # creates a new person identity and copies the outer dictionary

    copy_person['name'] = "Alice" # should mutate only the copy_person

    copy_person['skills'].append('FastAPI') # mutates the two, namely person and copy_person

    print(person)
    print(copy_person) 



if __name__ == '__main__':
    main()