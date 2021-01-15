"""
Binary Tree: is a tree datastructure where each node have have two children called as left-child and right-child 
!Eg:                            1 ---> Root Node
                              /   \
                            3      5 ---> Parent Node
                          /  \    /  \
         Left child<--- 6     2  8    4--->Right child   1)Pre-order:-1-3-6-7-9-2-5-8-4-11-30
                      /  \           /  \                2)In-order :-7-6-9-3-2-1-8-5-11-4-30
                    7     9         11   30              3)Post-ordr:-7-9-6-2-3-8-11-30-4-5-1
                                                         4)Level-Order:-1-3-5-6-2-8-4-7-9-11-30
Types of Binary tree: 1) complete binary tree : where every node have two children except is None the last may be have a left child or 
                      2) Full binary tree: In this every node have two children and also called as plane binary 

Types of Tree traversal:A)Depth First Order -1) Pre-order traversal  (Root-> Left-> Right)
                                             2) In-order traversal   (Left-> Root-> Right)
                                             3) Post-order traversal (Right-> Left-> Root)
                        B)Level Order Travesal :- Traverse's each level form left node to right node
"""
from Collection import Stack, Queue

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def Print_Tree(self,traversal_type):
        if traversal_type=="preorder":
            return self.Preorder_traversal(tree.root,"")
        elif traversal_type=="inorder":
            return self.Inorder_traversal(tree.root,"")
        elif traversal_type=="postorder":
            return self.Postorder_traversal(tree.root,"")
        elif traversal_type=="levelorder":
            return self.Levelorder_traversal(tree.root)
        else:
            print(f"{traversal_type} is Supported\nType-preorder,postorder,inorder")
            return False

    def Preorder_traversal(self,start,traversal:str):  #* traversal : Intial it will be an empty string for evry recursive call it will be updated and 
        """                                                #* at the end it will contain all values of the tree
        Root-> Left-> Rigth 
        """
        if start:
            traversal+=f"{start.value}-"
            traversal=self.Preorder_traversal(start.left,traversal)
            traversal=self.Preorder_traversal(start.right,traversal)
        return traversal

    def Inorder_traversal(self,start,traversal):
        """ Left-> Root-> Right """
        if start:
            traversal=self.Inorder_traversal(start.left,traversal)
            traversal+=f"{start.value}-"
            traversal=self.Inorder_traversal(start.right,traversal)
        return traversal
    
    def Postorder_traversal(self,start,traversal):
        """ Left-> Right-> Root"""
        if start:
            traversal=self.Postorder_traversal(start.left,traversal)
            traversal=self.Postorder_traversal(start.right,traversal)
            traversal+=f"{start.value}-"
        return traversal

    def Levelorder_traversal(self,start):
        queue=Queue()
        queue.enqueue(start)
        traversal =""
        while len(queue)> 0:
            traversal +=f"{queue.peek().value}-"  # Inserting the first value of the queue
            node=queue.dequeue()  # Storing the recent which was removed from the queue and 
            if node.left:         # asking does it have a left node
                queue.enqueue(node.left) # If yes then we are appending that value and same for the right node
            if node.right:
                queue.enqueue(node.right)
        return traversal 
    
    def reverse_levelorder(self,start):
        queue=Queue()
        queue.enqueue(start)
        stack=Stack()
        traversal =""
        while len(queue)>0:
            node=queue.dequeue()
            stack.push(node.value)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while stack:
            traversal+=f"{stack.pop()} "
        return traversal

    def Binarytree_length(self,Node)-> int:  # Node :from which you want to calculate height
        """ Returns the Lenght of longest chain in Binary tree"""                              
        if not Node:
            return -1
        left_height=self.Binarytree_length(Node.left)
        right_height=self.Binarytree_length(Node.right)                              #                      3 <-- 1 ---> 3
        return 1+(max(left_height,right_height))                                     #                          /   \
                                                                                     #                    2 <--3      5 ---> 2
                                                                                     #                       /  \    /  \
                                                                                     #              1 <--- 6     2  8    4--->1   
                                                                                     #                   /  \           /  \               
                                                                                     #                   7     9         11   30  
    def size(self):
        """ Returns the total Number of Nodes in the tree"""
        stack=Stack()
        stack.push(self.root)
        size=1
        while len(stack)>0:
            node=stack.pop()
            if node.left:
                size+=1
                stack.push(node.left)
            if node.right:
                size+=1
                stack.push(node.right)
        return size

if __name__ == "__main__":
    tree=BinaryTree(1)
    tree.root.left=Node(3)
    tree.root.right=Node(5)
    tree.root.left.left=Node(6)
    tree.root.left.right=Node(2)
    tree.root.left.left.left=Node(7)
    tree.root.left.left.right=Node(9)
    tree.root.right.left=Node(8)
    tree.root.right.right=Node(4)
    tree.root.right.right.left=Node(11)
    tree.root.right.right.right=Node(30)



    print(tree.Print_Tree("preorder"))
    print(tree.Print_Tree("inorder"))
    print(tree.Print_Tree("postorder"))
    print(tree.Print_Tree("levelorder"))
    print(tree.reverse_levelorder(tree.root))
    print(tree.Binarytree_length(tree.root))
    print(tree.size())