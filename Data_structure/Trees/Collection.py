class Stack:
    def __init__(self) -> None:
        self.items=[]

    def push(self,item):
        return self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items)==0

    def __len__(self):
        return self.size()

    def print_list(self):
        print(self.items)
        
    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        return self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items)==0

    def __len__(self):
        return self.size()

    def print_list(self):
        print(self.items)
        
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.peek())
