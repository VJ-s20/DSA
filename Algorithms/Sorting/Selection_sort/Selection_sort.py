"""
In Selection sort we first find a smallest element in the unsorted list and place it at the end of the sorted sublist. The process contiue's untill the list is fully sorted 
!Eg:             [3, 5, 7, 2, 8, 1]-> Unsorted list
                 [1, 5, 7, 2, 8, 3]
    sorted sublist_| |_Unsorted sublist  
                 [1, 2, 7, 5, 8, 3] 
                 [1, 2, 3, 5, 8, 7] 
                 [1, 2, 3, 5, 8, 7] 
!                [1, 2, 3, 5, 7, 8]->  Fully sorted list                                                                         
"""


def selection_sort(lst):
    for i in range(len(lst)-1):
        min_pos = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_pos]:
                min_pos = j
        lst[i], lst[min_pos] = lst[min_pos], lst[i]
    return lst



if __name__ == "__main__":
    lst1=["vijay","karan","ambuj","rahul","mishra"]
    lst2 = [3, 5, 7, 2, 8, 1]
    ss = selection_sort(lst2)
    print(ss)
