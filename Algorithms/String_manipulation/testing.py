# def rotLeft(a, d):
#     return a[d:]+a[:d]
    

# print(rotLeft([1,2,3,4,5,],4))

# def minimumBribes(q):
#     birbe=0
#     for i in range(len(q)-1):
#         if q[i]!=i+1:
#             q[i],q[i+1]=q[i+1],q[i]
#             birbe+=1
#     return birbe

# print(minimumBribes([2,5,1,3,4]))

# def riddle(arr):
#     # complete this function
#     n=0
#     values=[]
#     while n<len(arr):
#         for i in range(len(arr)-n):
#             values.append(arr[i])

#     print(values)

# riddle([1,2,3])

# def printFibb(n):
#     # your code here
#     first=0
#     second=1
#     for _ in range(n):
#         next=first+second
#         first=second
#         second=next
#         print(first)
# printFibb(7)

# def balancedSums(arr):
#     mid=(len(arr)//2)
#     if sum(arr[:mid])==sum(arr[mid+1:]):
#         return "YES"
#     return "NO"

# arr=[2,0,0,0]
# print(balancedSums(arr))



def recur(n):
    if n==0:
        return 1
    return n*recur(n-1)
print(recur(3))






























