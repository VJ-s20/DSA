
"""
Inital - 1 2 3 4 5
Birbed - 2 1 5 3 4 
"""
queue=[1,2, 5, 3, 7, 8, 6, 4]
queue=[2,1,5,3,4]


def print_helper(intial,final,name):
    print(f"{name}: Moved to {final} to {intial}")

def minimumBribes(q):
    birbes=0
    for i in range(len(q)-1):
        val=q[i]-i
        if val>3:
            return "TOO chaotic"
        for j in range(i+1,len(q)):
            birbes+=q[j]-i
        
    return birbes
print(minimumBribes(queue))

