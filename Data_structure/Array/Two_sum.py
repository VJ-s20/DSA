"""
Two sum problem :- You are given a target and a sorted list add any two elemt and return the elemns who's sum equal to the target
"""
arr,target=[-2,1,2,3,4,11],3

# * Approch 1:-Brute force 
#! Time complexity-O(n^2)
#! space complexity -O(1)

def brute_force_two_sum(arr,target):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                print(arr[i],arr[j])
                return True
    return False



# *Approch 2- Using heap Table
#! Time complexity- O(n)
#! space complexity - O(n)

def hash_table_two_sum(arr,target):
    ht=dict()
    for i in range(len(arr)):
        if arr[i] in ht:
            print(arr[i],ht[arr[i]])
            return True
        ht[target-arr[i]]=arr[i]
    return False



#* Approch 3: Two pointer technique Only if the list is sorted
# ! Time complexity - O(n)
#! space complexity - O(1)

def two_sum(arr,target):
    i=0  # Setting one pointer two zero  and 
    j=len(arr)-1 # second one at the last
    while i<j:
        if arr[i]+arr[j]==target:
            print(arr[i],arr[j])
            return True
        if arr[i]+arr[j]<target:  #** if the value of target is greater than sum of i and j then
            i+=1  #! we increament the staring pointer
        else: #* Else if target is less than sum of i and j then
            j-=1 #! we decrement j or we move 1 step back
    return False

# print(brute_force_two_sum(arr,target))
# print(hash_table_two_sum(arr,target))
print(two_sum(arr,target))
