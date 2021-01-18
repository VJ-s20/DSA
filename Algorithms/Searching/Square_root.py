'''
problem: You are given a number your task is to find the closest Square root val or equal to the target
'''
k=289
#  Retuns :17

#* Linear approch
def square_root_(k):
    close_val=0
    for i in range(k):
        if i**2 <=k:
            close_val=max(close_val,i)
    return close_val




# * Binary approch 
def square_root(k):
    low=1
    high=k
    while low<=high:
        mid=(low+high)//2
        mid_squared=mid*mid
        if mid_squared<=k:
            low=mid+1
        else: 
            high=mid-1
    return low-1
# print(square_root_(k))
print(square_root(k))