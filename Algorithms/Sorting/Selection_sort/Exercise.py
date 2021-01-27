elements=[
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]



def seletion_sort(lst,key):
    for i in range(len(lst)-1):
        min_val=i
        for j in range(i+1,len(lst)):
            if lst[j][key]<lst[min_val][key]:
                min_val=j
        lst[i],lst[min_val]=lst[min_val],lst[i]
    return lst

if __name__=="__main__":
    ss=seletion_sort(elements,'First Name')
    [print(i) for i in ss]
                