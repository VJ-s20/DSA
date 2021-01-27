"""
Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
Once both sub list have one elemnt we start comparing both sublist.
! Eg:                                   [5,3,6,1,8,2]-> Unsorted List
                                       [5,3,6    1,8,2]
*                       Left unsorted sublist   Right unsorted sublist
                                     [3, 5, 6]   [1, 2, 8]
*                            Sorted leftsublist  Sorted RightSublist
!                                      [1, 2, 3, 5, 6, 8]
                                       Merged Sorted Listt

"""


def Merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        left_lst = lst[:mid]
        right_lst = lst[mid:]
        Merge_sort(left_lst)
        Merge_sort(right_lst)
        i = j = k = 0   # i is the position of the left Sublist, j is the position of the right sublist and k is the position of the sorted list
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst[k] = left_lst[i]
                i += 1
                k += 1
            else:
                lst[k] = right_lst[j]
                j += 1
                k += 1
        while i < len(left_lst):  # If there are some elements left in the left sublist
            lst[k] = left_lst[i]
            i += 1
            k += 1
        while j < len(right_lst): # If there are some elements left in the right sublist
            lst[k] = right_lst[j]
            j += 1
            k += 1
        return lst


if __name__ == "__main__":
    lst = [5, 3, 6, 1, 8, 2]
    ms = Merge_sort(lst)
    print(ms)
