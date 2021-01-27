elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

def Bubble_sort(lst,key):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j+1][key]<lst[j][key]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst

if __name__=="__main__":
    bs=Bubble_sort(elements,'transaction_amount')
    bs=Bubble_sort(elements,'name')
    [print(i) for i in bs]