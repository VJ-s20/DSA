"""
In doubly linkedlist we have an extra pointer which points back to the previous node 
!Eg:None<--HEAD<==>data<==>data-->None
            Node
"""



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedlist:
    def __init__(self):
        self.head=None

    def prepend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    
    def append(self,data):
        if not self.head:
            self.head=Node(data)
            self.prev=None
        else:
            new_node=Node(data)
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new_node
            new_node.prev=curr

    def insert(self,pos,data):
        new_node=Node(data)
        if pos==0:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            return
        # inserting other than head position
        curr=self.head
        prev=None
        count=0
        while curr and count<pos:
            prev=curr
            curr=curr.next
            count+=1
        if not curr:
            print("position not available")
            return
        prev.next=new_node
        new_node.prev=prev
        curr.prev=new_node
        new_node.next=curr

    def sortedInsert(self, data):
        new_node=Node(data)
        if new_node.data<self.head.data:
            new_node.next=self.head
            self.head=new_node
            return 
        curr=self.head
        prev=None
        while curr:
            if data< curr.data:
                new_node.prev=prev
                new_node.next=curr
                prev.next=new_node
                return 
            prev=curr
            curr=curr.next
        prev.next=new_node
        new_node.prev=prev

    def print_list(self):
        curr=self.head
        prev=None
        while curr:
            prev=curr
            print(curr.data)
            curr=curr.next
        # while prev:
        #     print(prev.data)
        #     prev=prev.prev

    def delete(self,key):
        if key==self.head.data:    
            if not self.head.next:  #! case 1 :if want to delete the head node which does not have the next node
                self.head=None
            else:                     #* case2: if the head pointer had next node
                self.head=self.head.next
                self.head.prev=None
            return 
        curr=self.head
        prev=None
        while curr and curr.data!=key:
            prev=curr
            curr=curr.next
        if not curr:
            print("position not available")
            return
        if curr.next:  #* Case3: if node which we want to delete has a next node
            nxt=curr.next
            prev=curr.prev
            prev.next=nxt
            nxt.prev=prev  
            curr=None
        if not curr.next:  #* Case4: if node which we want to delete is last node
            prev.next=curr.next
            curr.prev=None
            curr=None

    def delete_node(self,node):
        if node==self.head:    
            if not self.head.next:  #! case 1 :if want to delete the head node which does not have the next node
                self.head=None
            else:                     #* case2: if the head pointer had next node
                self.head=self.head.next
                self.head.prev=None
            return 
        curr=self.head
        prev=None
        while curr and curr!=node:
            prev=curr
            curr=curr.next
        if curr.next:  #* Case3: if node which we want to delete has a next node
            nxt=curr.next
            prev=curr.prev
            prev.next=nxt
            nxt.prev=prev  
            curr=None
        else:  #* Case4: if node which we want to delete is last node
            prev.next=curr.next
            curr.prev=None
            curr=None

    def __len__(self):
        curr=self.head
        count=0
        while curr:
            count+=1
            curr=curr.next
        return count
# Reversing the doubly linkedlist
    def reverse(self):
        start=time.clock()
        curr=self.head
        tmp=None
        while curr:
            tmp=curr.prev
            curr.prev=curr.next
            curr.next=tmp
            curr=curr.prev
        if tmp:
            self.head=tmp.prev
        print(f"Time taken:{time.clock() - start}")
    def reverse_recursion(self):

        start=time.clock()
        def reverse(head):
            head.next,head.prev=head.prev,head.next 
            if not head.prev:
                return head
            return reverse(head.prev)
        self.head=reverse(self.head)
        print(f"Time taken:{time.clock()-start}")
# Removing the duplicates 
    def reomve_dup(self):

        curr=self.head
        seen=dict()
        while curr:
            if curr.data in seen.keys():
                nxt=curr.next
                self.delete_node(curr)
                curr=nxt
            else:
                seen[curr.data]=1
                curr=curr.next
#* pair of sum : In this problem we are given a val we want sum of two numbers to be equal to that number 
    def Pair_of_sum(self,sum_val):
        p,q=self.head,None
        pairs=[]
        while p:
            q=p.next  #* starting with 1 step ahead of p every time 
            while q:
                if p.data+q.data==sum_val:
                    pairs.append((p.data,q.data))
                q=q.next
            p=p.next  
        return pairs
        
import time      
if __name__ == "__main__":
    dlist=DoublyLinkedlist()
    dlist.append(1)
    dlist.append(2)
    dlist.append(2)
    dlist.append(2)
    dlist.append(4)
    dlist.append(3)
    dlist.append(5)
    dlist.append(5)
    dlist.append(5)
    dlist.append(5)
    # dlist.prepend(0)
    # dlist.insert(1,7)
    dlist.reomve_dup()
    dlist.reverse()
    dlist.print_list()
    print("\n\n")
    # dlist.delete(5)
   
    dlist.reverse_recursion()
    # print(dlist.Pair_of_sum(5))
    dlist.print_list()
    # print("\n\n")
    # print(len(dlist))