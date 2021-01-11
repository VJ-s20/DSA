"""
In Singly LinkedList a node consist of two items one is data and another is next where data is the item and the next points towards the next node the last next node always points to None(Null)
!Eg: Head->data|next-->data|next-->data|next-->None(Null)
*            Node         Node        Node
Linked list are non contigous memory, So
Accessing an item in LL in worst case is O(n) while in arrays it's O(1)
Inserting an item in LL is O(1) while in arrays it's O(n)
"""

from os import curdir


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
#* Inserting a node in the Linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:   #* if the list is empty the head will point at starting node
            self.head = new_node
            return
        last_node = self.head     #* Intial the head will point at the first item so in order to insert item in the last
        while last_node.next:     #* we need to shift the head pointer to the right untill it points to the null
            last_node = last_node.next
        last_node.next = new_node  #* Once we reach at the last node we can append the new node which will be now pointing to None
  
    def prepend(self,data):
        """
        Adding the new node to the front of the Linked list
        """
        new_node=Node(data)
        new_node.next=self.head #* Point to the current node 
        self.head=new_node

    def insert(self,pos,data):
        new_node=Node(data)
        if pos==0:
            new_node.next=self.head
            self.head=new_node
            return 
        curr=self.head
        prev=None
        count=0
        while curr and count<pos:
            prev=curr
            curr=curr.next
            count+=1
        if not curr:
            print("Position not avilable")
            return 
        prev.next=new_node
        new_node.next=curr


    def insert_after_node(self,prev_node,data):
        """
        Inserting in between the nodes
        """
        if not prev_node:
            print(f"There is no prev Node")
            return 
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node
# Deleting a node form the linked list
    def delete(self,key):  # key is the Node we want to delete
        curr_node=self.head
        if curr_node and curr_node.data==key: # Deleting the head node 
            self.head=curr_node.next
            curr_node=None
            return 

        prev=None                              # Deleting other nodes in the Ll 
        while curr_node and curr_node.data!=key:
            prev=curr_node
            curr_node=curr_node.next
        if curr_node is None:
            print("NODE not present")
            return 

        prev.next=curr_node.next
        curr_node=None

    def delete_at_pos(self,pos):
        curr_node=self.head
        if pos==0:
            self.head=curr_node.next
            curr_node=None
            return
        prev=0
        count=0
        while curr_node and count!=pos:
            prev=curr_node
            curr_node=curr_node.next
            count+=1
        if curr_node is None:
            return 
        prev.next=curr_node.next
        curr_node=None
# Lenght of the linked list
    def len_iter(self):
        curr_node=self.head
        iter_len=0
        while  curr_node:
            curr_node=curr_node.next
            iter_len+=1
        return iter_len
    
    def recur_len(self,node):
        if node is None:
            return 0
        return 1+self.recur_len(node.next)
# Swapping two nodes in a Linked list
    def swap_nodes(self,key_1,key_2):
        if key_1==key_2:
            print("Swapped succesfully")
            return 
        prev_node1=None
        curr_node1=self.head 
        while curr_node1 and curr_node1.data !=key_1:
            prev_node1=curr_node1
            curr_node1=curr_node1.next
        prev_node2=None
        curr_node2=self.head
        while curr_node2 and curr_node2.data!=key_2:
            prev_node2=curr_node2
            curr_node2=curr_node2.next
        
        if prev_node1:
            prev_node1.next=curr_node2
        else:
            self.head=curr_node2
        if prev_node2:
            prev_node2.next=curr_node1
        else:
            self.head=curr_node1
        curr_node1.next,curr_node2.next=curr_node2.next,curr_node1.next

    @staticmethod
    def print_helper(node,name):
        if node is None:
            print(f"{name}: None")
        else:
            print(f"{name}:{node.data}")

# Reversing the linked list iterative and recursive
    def reverse_iter(self):
        prev=None
        curr=self.head
        while curr:
            nxt=curr.next
            curr.next=prev
            self.print_helper(prev,"prev")
            self.print_helper(curr,"curr")
            self.print_helper(nxt,"Next")
            print("\n")
            prev=curr
            curr=nxt
        self.head=prev

    def reverse_recursive(self):
        def _reverse_recursive(curr,prev):
            if not curr:
                return prev
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            return _reverse_recursive(curr,prev)

        self.head=_reverse_recursive(curr=self.head,prev=None)

# * Merging two sorted list
# ! It's necessary that both the list should be sorted else the output will not be a sorted list
    def merge_sorted(self,llist):
        p=self.head
        q=llist.head
        s=new_head=None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data<=q.data:
                s=p
                p=s.next
            else:
                s=q
                q=s.next
            new_head=s
        while p and q:
            if p.data<=q.data:
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next
        if not p:
            s.next=q
        if not q:
            s.next=p
        return new_head

    def remove_dup(self):
        curr=self.head
        prev=None
        dup_values=dict()
        while curr:
            if curr.data in dup_values:
                # removing the node 
                prev.next=curr.next
                curr=None
            else:
                # if do not encounter any dup vaules
                dup_values[curr.data]=1
                prev=curr
            curr=prev.next
    def __len__(self):
        curr=self.head
        count=0
        while curr:
            count+=1
            curr=curr.next
        return  count
    def Nth_val(self):
        size=len(self)
        k=2
        curr=self.head
        while k<size:
            curr=curr.next
            k+=1
        return curr.data
# retriving a particular value
    def get_value(self,n):
        curr=self.head
        count=0
        while curr and count< n:
            curr=curr.next
            count+=1
        if not curr:
            return "value is greater than the linked list"
        return f"The value is: {curr.data} at {n}"

# COunting the occurancce of a particular data
    def iter_occ(self,data):
        curr=self.head
        occ=0
        while curr:
            if curr.data==data:
                occ+=1
            curr=curr.next
        return occ

    def recur_occ(self,node,data):
        if not node: return 0
        if node.data==data:
            return 1+self.recur_occ(node.next,data)
        else:
            return self.recur_occ(node.next,data)

#* Rotating the linked list form a given pos(pivot)
    def rotate(self,pvoit):
        p=q=self.head
        prev=None
        count=0
        while p and count<pvoit:
            prev=p
            p=p.next
            q=q.next
            count+=1
        p=prev
        while q:
            prev=q
            q=q.next
        q=prev
        q.next=self.head
        self.head=p.next
        p.next=None

#* checking if a linked list is palindrome or not
    def is_palindrome(self):
        #! Method 1 
        curr=self.head
        s=""
        while curr:
            s+=curr.data
            curr=curr.next
        return s==s[::-1]
        # # ! Method 2
        # curr=self.head
        # stack=[]
        # while curr:
        #     stack.append(curr.data)
        #     curr=curr.next
        # curr=self.head
        # while curr:
        #     data=stack.pop()
        #     if data!=curr.data:
        #         return False
        #     curr=curr.next
        # return True

    def move_tail_to_head(self):
        last=self.head
        second_to_last=None
        while last.next:
            second_to_last=last
            last=last.next
        last.next=self.head
        second_to_last.next=None
        self.head=last

    def sum_of_two_LL(self,llist):
        p=self.head
        q=llist.head
        num1=""
        while p:
            num1+=str(p.data)
            p=p.next
        num2=""
        while q:
            num2+=str(q.data)
            q=q.next
        return int(num1[::-1])+int(num2[::-1])

if __name__ == "__main__":
    Llist1 = LinkedList()
    Llist1.append(5)
    Llist1.append(6)
    Llist1.append(3)
    Llist1.append(8)
    # Llist2=LinkedList()
    # Llist2.append(8)
    # Llist2.append(4)
    # Llist2.append(2)
    # Llist1.rotate(4)
    # Llist1.move_tail_to_head()
    # print(Llist1.sum_of_two_LL(Llist2))
    # Llist1.reverse_ll()
    Llist1.print_list()
    print(Llist1.Nth_val())
