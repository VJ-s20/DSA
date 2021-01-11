'''
stack follows LIFO or FIFO 
In stack every time if we insert an item it will be insert at the top of the list and if we pop an item it will be pop the first item 
Basic operations are push pop peek 
eg:
A B C D
Inserting
D
C
B
A
poping
D
'''

class Stack:
    def __init__(self) :
        self.items=[]

    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items==[]

    def get_stack(self):
        print(self.items)

    def peek(self):
        return self.items[-1]

    
if __name__ == "__main__":
    s=Stack()
    print(s.is_empty())
    s.push("A")
    s.push("B")
    s.push("C")
    s.push("D")
    s.push("B")
    s.get_stack()
    s.pop()
    s.get_stack()
    s.get_stack()
    print(s.peek())
    print(s.is_empty())

