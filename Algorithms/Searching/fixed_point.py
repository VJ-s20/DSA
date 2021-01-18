"""
A fixed point in an array A such that A[i] is equal to index i
"""


# Linear approch 

def fixed_point(data):
    for i in range(len(data)):
        if data[i]==i:
            return data[i]
    return None


data=[-2,-1,0,1,3,4,6]
print(fixed_point(data))


# Binary approch  -O(logn)

def fixed_point(data):
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if data[mid]==mid: #* If the index of the data and the element are equal
            return mid
        elif data[mid]<mid:  #* if the index is greater than the data element then we know that the only posibilty of the index and the data elment to be equal is on the right side
            low=mid+1
        else:  #* visa versa
            high=mid-1
    return None

print(fixed_point(data))