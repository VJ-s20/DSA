"""
In Insertion sort we divide the list into two sublist one is sorted list and another is unsorted list.
After every iteration we take one element from the unsorted sublist and put into the sorted sublist and compare it from existing element present in the sorted sublist. The process continue untill the list is fully sorted
! Eg:                                          [3, 5, 1, 7, 8, 2]
                                Sorted sublist<__||__>Unsorted sublist
                                               [1, 3, 5, 7, 8, 2]
                                               [1, 3, 5, 7, 8, 2]
                                               [1, 3, 5, 7, 8, 2]
!                                              [1, 2, 3, 5, 7, 8]--> Fully sorted list

"""


def Insertion_sort(lst):
    for i in range(1,len(lst)):
        curr_ele=lst[i]
        pos=i
        while curr_ele<lst[pos-1] and pos>0:
            lst[pos]=lst[pos-1]
            pos-=1
        lst[pos]=curr_ele
    return lst

def runningTime(arr):
    count = 0
    for i in range(1,len(arr)):
        while arr[i]<arr[i-1] and i > 0:
            arr[i] , arr[i-1] = arr[i-1] , arr[i]
            count = count+1
            i = i-1
    return count

    
if __name__=="__main__":
    lst=[3,5,1,7,8,2]
    # lst=[2,1,3,1,2]
    # print(runningTime(lst))
    
    Is=Insertion_sort(lst)
    print(lst)
