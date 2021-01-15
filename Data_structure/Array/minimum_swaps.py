def minimumSwaps(arr):
    swaps=0
    for i in reversed(range(1,len(arr)-1)):
        if arr[i+1]<arr[i]:
            arr[i+1],arr[i]=arr[i],arr[i+1]
            swaps+=1
        elif arr[i-1]>arr[i]:
            arr[i-1],arr[i]=arr[i],arr[i-1]

    return arr

print(minimumSwaps([4, 3, 1, 2]))