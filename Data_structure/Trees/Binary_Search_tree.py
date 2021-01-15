"""
Binary Search Tree:-is Tree data Structure where each node can have a most of two children which are refered as left-child and right-child. 
                    Binarysearch differ more binarytree as the nodes are in Sorted.
!Eg:-             8-->Root
                /   \
              3       11       BST Property:Nodes lesser than the root node are on the left and Nodes greater than the root are on the Right.
            /  \     /  \ 
          1     6   9    13

"""
class Node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            return self._insert(data,self.root)

    def _insert(self,data,curr_node):
        if data<curr_node.data:
            if not curr_node.left:
                curr_node.left= Node(data) 
            else:
                return self._insert(data,curr_node.left)
        elif data>curr_node.data:
            if not curr_node.right:
                curr_node.right=Node(data) 
            else:
                return self._insert(data,curr_node.right)
        else:
            print("Node already availalbe!")
            return False

    def search(self,data):
        if self.root:
            is_found=self._search(data,self.root)
            if is_found:
                return True
            return False
        else:
            return None
    def _search(self,data,curr_node):
        if data < curr_node.data and curr_node.left:
            return self._search(data,curr_node.left)
        elif data> curr_node.data and curr_node.right:
            return self._search(data,curr_node.right)
        elif data== curr_node.data:
            return True

    def inorder_print(self):
        if self.root:
            return self._inorder(self.root)
    def _inorder(self,curr_node):
        if curr_node:
            self._inorder(curr_node.left)
            print(str(curr_node.data))
            self._inorder(curr_node.right)

    def BST_property(self):            
        if self.root:
            is_satisfied=self._BST_property(self.root,self.root.data)
            if is_satisfied is None:
                return True
            return False
        return True

    def _BST_property(self,curr_node,data):
        if curr_node.left:
            if data>curr_node.left.data:  # if the data i.e is the root is lesser thatn the left node
                return self._BST_property(curr_node.left,curr_node.left.data)  # if not than go for the next value
            else:
                return False # if yes than its violation of bst property
        if curr_node.right:  # same for right node
            if data<curr_node.right.data:
                return self._BST_property(curr_node.right,curr_node.right.data)
            else:
                return False
                
    def check_binary_search_tree_(self,root):
        def inOrder(root,traversal):
            if root:
                traversal=inOrder(root.left,traversal)
                traversal.append(root.data)
                traversal=inOrder(root.right,traversal)
            return traversal
        traversal=[]
        inOrder(root,traversal)
        return traversal==sorted(set(traversal))

    def leastCommon_Ancestor(self,val1,val2):
        root=self.root
        while True:
            if val1< root.data and val2 <root.data:
                root=root.left
            elif val1> root.data and val2>root.data:
                root=root.right
            else:
                return root.data
            

if __name__=="__main__":
    bst=BST()
    bst.insert(8)
    bst.insert(3)
    bst.insert(1)
    bst.insert(6)
    bst.insert(11)
    bst.insert(9)
    bst.insert(13)
    # print(bst.search(22))
    tree=BST()
    tree.root=Node(4)
    tree.root.left=Node(5)
    tree.root.right=Node(1)

    # bst.inorder_print()
    # print(bst.BST_property())
    # print(tree.BST_property())
    print(bst.leastCommon_Ancestor(bst.root.left.right.data,bst.root.left.left.data))

        
