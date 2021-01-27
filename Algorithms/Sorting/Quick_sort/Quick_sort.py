"""
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.
1)Always pick first element as pivot.
2)Always pick last element as pivot (implemented below)
3)Pick a random element as pivot.
4)Pick median as pivot.
! Eg1:                  5 is the Pivot <-[5, 1, 3, 2, 8, 6]
                                         [2, 1, 3, 5, 8, 6]
*                                                  |_> Now 5 is Sorted as before 5 all element are lesser than him and after 5 all are bigger than him
                                         [1, 2, 3, 5, 8, 6]
!                                        [1, 2, 3, 5, 6, 8]-> Sorted list
"""


def pivot_place(arr, first, last):
    pivot = first
    left = first + 1
    right = last
    while True:
        while left <= right and arr[left] <= arr[
            pivot]:  # if the left element is greater than the pivot we break the loop
            left += 1
        while left <= right and arr[right] >= arr[
            pivot]:  # If the right element is lesser than the pivot we break the loop
            right -= 1
        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[
                left]  # Swapping the greater element in the left and lesser element in the right
    arr[pivot], arr[right] = arr[right], arr[pivot]  # Swapping the pivot element to the Sorted position
    return right


def Quick_sort(arr, first, last):
    if first < last:
        p = pivot_place(arr, first, last)  # Finding the mid element from the list
        Quick_sort(arr, first, p - 1)  # Left sublist
        Quick_sort(arr, p + 1, last)  # Right sublist
    return arr


if __name__ == "__main__":
    lst = [5, 1, 3, 2, 8, 6]
    arr = [4, 5, 3, 7, 2]
    qs = Quick_sort(lst, 0, len(lst) - 1)
    print(qs)
