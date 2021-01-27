'''
Task: You are given a arry you have to find the minmum number in the array 
Input: [4,5,6,7,1,2,0]
Returns: 0
'''
data=[4,5,6,7,1,2,0]

def lowest_point(data):
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if data[mid]>data[high]:
            low=mid+1
        else:
            high=mid-1
    return data[low]

print(lowest_point(data))



