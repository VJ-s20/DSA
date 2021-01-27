"""
Bubble sort is the easiest sorting algorithm with the Time complexity: O(n^2) and space complexity : O(1)
In bubble sort the highest element goes to the end of the list after every iteration. This process continue until the list is fully sorted
! Eg: [3, 5, 2, 8, 1]-> Unsorted list
      [3, 2, 5, 1, 8]
      [2, 3, 1, 5, 8]
      [2, 1, 3, 5, 8]
!     [1, 2, 3, 5, 8]-> Fully sorted list

"""

def bubble_sort(lst):
    for i in reversed(range(len(lst))):
        swapped = False
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


if __name__ == "__main__":
    lst1 = ["vijay", "karan", "ambuj", "rahul", "mishra"]
    lst2 = [3, 5, 2, 8, 1]
    bs = bubble_sort(lst1)
    print(bs)
