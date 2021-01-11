from stack import Stack


def reversing(string):
    s=Stack()
    for i in range(len(string)):
        s.push(string[i])

    rev=""
    while not s.is_empty():
        rev+=s.pop()

    return rev


print(reversing("hello world"))

