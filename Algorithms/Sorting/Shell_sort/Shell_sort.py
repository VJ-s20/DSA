"""
Shell sort is a highly efficient sorting algorithm and is based on insertion sort algorithm.
This algorithm avoids large shifts as in case of insertion sort, if the smaller value is to the far right and has to be moved to the far left.
!Eg:                    [5, 8, 3, 2, 6, 1]->  gap=3
                        [2, 6, 1, 5, 8, 3]->  gap=1
!                       [1, 2, 3, 5, 6, 8]-> Sorted list
"""


def Shell_sort(arr):
    gap = len(arr)//2   
    while gap > 0:
        for i in range(gap, len(arr)):
            curr_ele = arr[i]
            pos = i
            while pos >= gap and curr_ele < arr[pos-gap]:
                arr[pos] = arr[pos-gap]
                pos -= gap
            arr[pos] = curr_ele
        gap = gap//2 
    return arr


def shellSort(lst):
    gap = len(lst)//2
    while gap > 0:
        for i in range(gap, len(lst)):
            while i >= gap and lst[i] < lst[i-gap]:
                lst[i], lst[i-gap] = lst[i-gap], lst[i]
                i -= gap
        gap //= 2
    return lst


if __name__ == "__main__":
    arr = [5, 8, 3, 2, 6, 1]
    print(Shell_sort(arr))
    print(shellSort(arr))
