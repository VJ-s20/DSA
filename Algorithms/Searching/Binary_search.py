"""
Binary Search : Binary search is beter than linear search if you have a sorted list and distinct values. It divide the list from the mid point
and if the mid point of the list is the target which we are lookiing for we simply return that else if the mid point 
is greater than the target we reduced the last pointer to mid -1  else we reduced the starting pointer
"""

data=[1,2,4,5,6,7,23,33,55,74,88,93,100]


#! Linear Search -O(n)
def linear_search(data,target):
    for i in range(len(data)):
        if data[i]==target:
            return True
    return False



# ! Binary search iterative  -O(logn)
def Binary_search_iterative(data,target):
    first=0
    last=len(data)-1
    while first<=last:
        mid=(first+last)//2
        if target==data[mid]:
            return True
        elif target<data[mid]:
            last=mid-1
        else:
            first=mid+1
    return False

# ! Binary search recursive  -O(logn)
def Binary_search_recursive(data,target,first,last):
    if first>last:
        return False
    mid=(first+last)//2
    if target==data[mid]:
        return True
    elif target<data[mid]:
        return Binary_search_recursive(data,target,first,mid-1)
    else:
        return Binary_search_recursive(data,target,mid+1,last)

print(linear_search(data,55))
print(Binary_search_iterative(data,55))

print(Binary_search_recursive(data,55,0,len(data)-1))
