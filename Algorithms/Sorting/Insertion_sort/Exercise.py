elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

def Insertion_sort(lst,key):
    for i in range(1,len(lst)):
        curr_ele=lst[i]
        pos=i
        while curr_ele[key]<lst[pos-1][key] and pos >0:
            lst[pos]=lst[pos-1]
            pos-=1
        lst[pos]=curr_ele
    return lst



if __name__ =="__main__":    
    Is=Insertion_sort(elements,'age')
    [print(i) for i in Is]
