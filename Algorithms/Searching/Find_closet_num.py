"""
Problem: You are given a sorted list  and a target value your task is to find the closest val in the list 
example: a=[1,2,4,5,8,10,13,15]
target= 11
output: 10
"""

#! Linear search 
def linear_approch(data,target):
    min_diff=float("inf")
    close=None
    for i in range(len(data)):
        if min_diff>abs(data[i]-target):
            min_diff=abs(data[i]-target)
            close=data[i]
    return close

#! Binary search 
def find_closest_num(data,target):
    min_diff=float("inf") # Setting the min difference to infinity
    low=0
    high=len(data)-1
    closest_num=None

    if len(data)==0:
        return None
    elif (len(data))==1:
        return data
    while low<=high:
        mid=(low+high)//2

        if mid+1<len(data):  # making sure that the mid right val does not exceeds the lenght of data
            min_diff_right=abs(data[mid+1]-target)
        if mid>0:
            min_diff_left=abs(data[mid-1]-target)

        if min_diff>min_diff_right:
            min_diff=min_diff_right
            closest_num=data[mid+1]
        elif min_diff>min_diff_left:
            min_diff=min_diff_left
            closest_num=data[mid-1]        
        
        if target<data[mid]:
            high=mid-1
        elif target>data[mid]:
            low=mid+1
        else:  # if the value which we are looking for is equal to the curr val
            return data[mid]
    return closest_num

a=[1,2,4,5,8,10,13,15]
target=20
y=find_closest_num(a,target)
print(linear_approch(a,target))
print("\n\n")
print(y)



