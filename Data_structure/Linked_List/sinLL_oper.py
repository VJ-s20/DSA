from singly_LL import LinkedList

# # * mergeing two sorted list
# Llist1=LinkedList()
# Llist1.append(1)
# Llist1.append(2)
# Llist1.append(3)
# # Llist1.append(8)
# Llist2=LinkedList()
# Llist2.append(1)
# # Llist2.append(3)
# # Llist2.append(4)
# # Llist2.append(6)

# Llist1.merge_sorted(Llist2)
# Llist1.print_list()

# # * Other operations
# llist=LinkedList()
# llist.append(1)
# llist.append(1)
# llist.append(1)
# llist.append(1)
# llist.append(1)
# llist.append(2)
# llist.append(6)
# llist.append(3)
# llist.append(4)
# llist.append(5)

# llist.remove_dup() # Removing duplicates

# llist.rotate(4)    # Rotating the list from a point

# llist.print_list()
# * checking is a linked list is palindrome or not
# Llist=LinkedList()
# Llist.append("M")
# Llist.append("O")
# Llist.append("M")
# Llist.append("M")
# print(Llist.is_palindrome())

# Llist=LinkedList()
# Llist.append("A")
# Llist.append("B")
# Llist.append("C")
# Llist.append("D")
# Llist.insert(3,"E")   # INserting at given location except the last position
# # * Moving the tail to front
# Llist.move_tail_to_head()
# Llist.print_list()

# print(llist.get_value(2))      # Retriving a value from linked list
# print(llist.recur_occ(llist.head,1))

# Llist.reverse_iter()
# Llist.reverse_recursive()
# Llist.print_list()
# Llist.insert_after_node(Llist.head.next,"E")
# print(Llist.recur_len(Llist.head))

#* swaping the nodes
Llist=LinkedList()
Llist.append("A")
Llist.append("B")
Llist.append("C")
Llist.append("D") 
# Llist.swap_nodes("B","C")
Llist.reverse_ll()
Llist.print_list()


# exit()
# print("1-to append 2-prepend 3-delete at node 4-delete at a position\n\t 5-for len of Linked list 6-swap nodes 7-print linkedlist 8-Exit")
# while True:
#     ask=int(input("->"))
#     if ask==1:
#         n=input("Enter a node a append:")
#         Llist.append(n)
#     elif ask==2:
#         n=input("Enter a node to prepend:")
#         Llist.prepend(n)
#     elif ask==3:
#         n=input("Enter a node to delete:")
#         Llist.delete(n)
#     elif ask==4:
#         n=input("Enter a pos to delete:")
#         Llist.delete_at_pos(int(n))
#     elif ask==5:
#         print("Length of linkedlist is:-",Llist.len_iter())
#     elif ask==6:
#         Llist.swap_nodes(input("key1:"),input("key2:"))
#     elif ask==7:
#         Llist.print_list()
#     elif ask==8:
#         break
#     else:
#         print("Invalid choice")