"""
A circular Linked list is similar to singly linkedlist but in CircularLL the last node points to the head of the list instead of pointing to None(null)
!Eg: Head->data|next->data|next->data|next--.
!              |____________________________| 
"""

class Node:
    def __init__(self,data) -> None:
        self.data=data 
        self.next=None
        
class CircularLinkedlist:
    def __init__(self):
        self.head=None
    
    def prepend(self,data):
        new_node=Node(data)
        curr=self.head
        new_node.next=self.head
        while curr.next!=self.head:
            curr=curr.next
        curr.next=new_node
        self.head=new_node

    def append(self,data):
        if self.head is None:    # If the list is empty 
            self.head=Node(data) 
            self.head.next=self.head
        else:
            new_node=Node(data)
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next
            curr.next=new_node
            new_node.next=self.head

    def insert_bet_nodes(self,pos,data):
        new_node=Node(data)
        curr=self.head
        prev=None
        if pos==0:
            new_node.next=self.head          # IF we want to insert at the head 
            while curr.next!=self.head:
                curr=curr.next
            curr.next=new_node
            self.head=new_node
        else:
            count=0
            while curr.next!=self.head and count<pos:
                prev=curr
                curr=curr.next
                count+=1
            if curr.next==self.head:
                print("Position not available")
                return 
            prev.next=new_node
            new_node.next=curr

    def Print_list(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next
            if curr==self.head:
                break
#* Deleting a node form a circular linked list
    def delete(self,key):
        curr=self.head
        prev=None
        if curr.data==key:
            while curr.next!=self.head:     # if we want to delete at first node
                curr=curr.next
            curr.next=self.head.next
            self.head=self.head.next
            return
        while curr.next!=self.head and curr.data!=key:  
            prev=curr
            curr=curr.next
        if curr.next==self.head:
            print("Node not available")
            return 
        prev.next=curr.next
        curr=None
    def remove_node(self,data):
        curr=self.head
        prev=None
        if curr==data:
            while curr.next!=self.head:     # if we want to delete at first node
                curr=curr.next
            curr.next=self.head.next
            self.head=self.head.next
            return
        while curr.next!=self.head and curr!=data:  
            prev=curr
            curr=curr.next
        prev.next=curr.next
        curr=None

# * length of the circular liked list
    def __len__(self):
        curr=self.head
        count=0
        while curr:
            curr=curr.next
            count+=1
            if curr==self.head:
                break
        return count

# * splitting the list from the mid point
    def split_clist(self):
        size=len(self)
        if size==0:   # If the list is empty
            return 
        if size==1: # if the list has only one node
            return self.head
        curr=self.head
        prev=None
        count=0
        mid=size//2   # Mid point of the list from where we want to split the list
        while count<mid:
            prev=curr
            curr=curr.next
            count+=1
        prev.next=self.head    # the fist cirular list
        split_cells=CircularLinkedlist()  # the second splited list
        while curr.next!=self.head:      # NOw the curr the second splited list
            split_cells.append(curr.data)
            curr=curr.next
        split_cells.append(curr.data)
        self.Print_list()
        print("\n")
        split_cells.Print_list()

    
#* josephus problem: you are given a step if step == to the node position of the node remove
#* that node keep doing it untill there is only one node left
    def josephus_circle(self,step):
        curr=self.head
        while len(self)>1:
            count=1
            while count!=step:
                count+=1
                curr=curr.next
            print(f"Removed: {curr.data}")
            self.remove_node(curr)
            curr=curr.next
            
#? Checking if the list is circular or not
    def is_circular(self,input_list):
        curr=input_list.head
        while curr.next:
            if curr.next==input_list.head:
                return True
            curr=curr.next 
        return False

    def reverse(self): #! Unsolved
        curr=self.head
        prev=None
        while curr.next!=self.head:
            # if curr.next==self.head:
            #     curr.next=self.head
            #     self.head=curr
            #     break
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        curr.next=self.head
        self.head=curr

if __name__ == "__main__":
    clist=CircularLinkedlist()
    clist.append("A")
    clist.append("B")
    clist.append("C")
    clist.append("D")
    # clist.prepend("B")
    # clist.insert_bet_nodes(0,"A")
    # clist.insert_bet_nodes(2,"C")
    # clist.Print_list()
    # print("\n\n")
    # cirular.delete("A")
    # print(len(cirular))
    # clist.split_clist()
    # clist.Print_list()
    # clist.remove_node(clist.head.next)
    # clist.josephus_circle(4)
    # clist.Print_list()
    from singly_LL import LinkedList
    llist=LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.reverse_iter()
    llist.print_list()
    # print(clist.is_circular(clist))
    # print(clist.is_circular(llist))
    # print(clist.reverse())
    # clist.Print_list()
