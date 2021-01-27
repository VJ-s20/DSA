"""
Input:[1,2,3,4]
Retuns:[[1, 2], [2, 3], [3, 4]] len(of this list)
"""

# Linear: O(n)
def pairs(k, arr):
    count=0
    low=0
    high=1
    while high<len(arr):
        diff=abs(arr[low]-arr[high])
        if diff<k:
            high+=1
        elif diff>k:
            low+=1
        else:
            count+=1
            high+=1

    return count
    
# Brute force :O(n^2)  
def pairs_brute_force(k,arr):
    pairs=[]
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if abs(arr[i]-arr[j])==k:
                pairs.append([arr[i],arr[j]])
    return pairs
arr=[1,2,3,4]
print(pairs(1,arr))
print(pairs_brute_force(1,arr))