"""
Counting sort is a sorting technique based on keys between a specific range.
It works by counting the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output sequence.
"""


def countSort(arr):
    count=[0]*(max(arr)+1)
    for i in arr:
        count[i]+=1
    sortedarr=[]
    for j in range(len(count)):
        while count[j]!=0:
            sortedarr.append(j)
            count[j]-=1
    return sortedarr


if __name__=="__main__":
    arr=[5,3,2,6,4,1,5,0]
    print(countSort(arr))
