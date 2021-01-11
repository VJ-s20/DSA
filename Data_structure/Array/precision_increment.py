"""
Arbitary precision increment :- Add 1 in the last element if it equls to 10 then make it 0 and add that one to the previous elemnt and 
! if the 1st element ==10 then make if 1 and add zero in the last  
"""

def presion_increment(arr):
    arr[-1]+=1     # Adding 1 in the last elemt 
    for i in reversed(range(1,len(arr))):  # Reversing cheking the list
        if arr[i]!=10: # IF the element does not equal to 10 then we simply break the loop
            break
        arr[i]=0
        arr[i-1]+=1
        if arr[0]==10:  # If the 1 element ==10 then 
            arr[0]=1  # make it 1 and 
            arr.append(0)  # append zero in the last
    return arr


print(presion_increment([1,4,9]))
print(presion_increment([9,9,9]))