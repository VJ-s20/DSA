
"""
Inital - 1 2 3 4 5
Birbed - 2 1 5 3 4 
"""
queue=[1,2, 5, 3, 7, 8, 6, 4]
queue=[2,1,5,3,4]




def minimumBribes(q):
    birbes=0
    for i in range(len(q)):
        if q[i]-i>3:
            return "TOO chaotic"
        for j in range(max(0,q[i]-2),i):
            if q[j]>q[i]:
                birbes+=1
        
    return birbes
print(minimumBribes(queue))

