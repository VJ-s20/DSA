'''
Quene follows first in first out (FIFO)
Every item is inserted at the end of the list and item is removeed from the last of the list
eg. imagine standing in a line to buy something

'''


class Quene:
    def __init__(self) -> None:
        self.items=[]

    def quene(self):
        item=int(input("Enter item:>"))
        self.items.append(item)

    def deque(self):
        if not self.is_empty():
            print(self.items.pop(0))
        return print(self.is_empty())

    def is_empty(self):
        return not self.items
    
    def peek(self):
        if not self.is_empty():
            print(self.items[0])

    def gets(self):
        print(self.items)

    def __len__(self):
        return len(self.items)

if __name__ == "__main__":
    q=Quene()
    print("""1 to insert item. 2 to pop item 4 to print quene 3. to peek item """)
    while True:
        ask=int(input(">"))
        if ask==1:
            q.quene()
        elif ask==2:
            q.deque()

        elif ask==3:
            q.peek()
        elif ask==4:
            q.gets()

        else:
            print("invalid choice")


