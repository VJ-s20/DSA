from stack import Stack
def binary(decimal):
    s=Stack()
    while decimal >0:
        reminder=decimal%2
        s.push(reminder)
        decimal=decimal//2

    bin_num=""
    while not s.is_empty():
        bin_num+=str(s.pop())

    return bin_num


print(binary(111))
# print(bin(215))

# Recursive approch to this problem

s=""
def binary(decimal):
    global s
    reminder=decimal%2
    s+=str(reminder)
    if decimal<1:
        return s[::-1]
    else:
        x=decimal//2
        return binary(x)
print(binary(111))


def binary_num(dec):
    s=[]
    while dec>0 :
        rem=dec%2
        s.append(str(rem))
        dec=dec//2

    return "".join(s[::-1])

print(binary_num(215))