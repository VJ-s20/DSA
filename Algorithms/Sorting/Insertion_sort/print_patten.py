"""
Input: [2,4,5,8,3]
Retuns : 2 4 5 8 8
         2 4 5 5 8
         2 4 4 5 8
         2 3 4 5 8
"""


def insertionSort1(n, arr):
    stored=arr[-1]
    last=n-1
    while last!=0 and stored<arr[last-1]:
        arr[last]=arr[last-1]
        print(*arr)
        last-=1
    arr[last]=stored
    print(*arr)

arr=[2,4,5,8,3]
n=5
insertionSort1(n,arr)