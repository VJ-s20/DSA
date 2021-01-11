"""
Advance Array game-you are given a arrys of elemnts you have to reach to the end of the arrys with moves <= to the element you are
"""

def Advance_array(arr):
    furthest_reached=0
    i=0
    last_elemnt=len(arr)-1
    while i<=furthest_reached and furthest_reached<last_elemnt:
        furthest_reached=max(furthest_reached,arr[i]+i)
        i+=1
    return furthest_reached>=last_elemnt


print(Advance_array([3,3,1,0,2,1,6]))

print(Advance_array([3,2,0,0,1,4]))  #! In this eg the max we can go is 3 and when i reahes 4 it becomes greater than furthest_reached than we can go which means we can't move ahead now