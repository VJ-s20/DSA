'''
Write a function that takes an array of sorted intergers and a key and returns 
the index of the first occurance of that key from the array 
example:-a=[-3,-1,0,2,4,5,6,7,7,23,43,55,399,399]
target=399
Returns: index 14
'''


a=[-3,-1,0,2,4,5,6,7,7,23,43,55,399,399]

# * Linear appoch O(n)
def find_occ(data,target):
    for i in range(len(data)):
        if data[i]==target:
            return i
    return None


print(find_occ(a,399))



# * Binary approch Best case - O(logn) 
#! worst case O(n)  if the list contains all same value or there are many duplicates of the target in the list
def find_first_occ(data,target):
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if data[mid]<target:
            low=mid+1
        elif data[mid]>target:
            high=mid-1
        else:
            if mid-1<0:
                return mid
            if data[mid]!=data[mid-1]:
                return mid
            high=mid-1
    return None

print(find_first_occ(a,399))