"""
Define a bitonic sequence as a sequence of intergers such that :
    x_1 <=....<=x_k>=.....x_n-1 for some k,0<=k< n
For example :
     1,2,3,4,5,4,3,2,1
is a bitonic sequnce.  Write a program to find the largest elemnt in such a sequence . In the examle above. the program should return "5"
We assume that such a peek element exists.
"""

data=[1,2,3,4,5,4,3,2,1]
data=[1,6,5,4,3,2,1]



# * Linear approch 

def bionic_nums(data):
    for  i in range(len(data)-1):
        if data[i]>data[i+1]:
            return data[i]
    return -1

print(bionic_nums(data))


#* Binary approch 

def Bionic_nums(data):
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        mid_left=data[mid-1] if mid>0 else float("-inf")
        mid_right=data[mid+1] if mid+1 <len(data) else float("inf")
        if mid_left<data[mid] and mid_right>data[mid]:
            low=mid+1
        elif mid_left>data[mid] and mid_right<data[mid]:
            high=mid-1
        elif mid_left<data[mid] and mid_right<data[mid]:
            return data[mid]
    return -1

print(Bionic_nums(data))
                


