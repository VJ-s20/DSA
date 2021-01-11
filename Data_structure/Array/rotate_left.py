# Using Queue logic
def rotLeft(a, d):
    for _ in range(d):
        a.append(a[0])
        a.pop(0)
    return a
a=[1,2,3,4,5]
d=4

print(rotLeft(a,d))

# ** Using python indexing 
a=[1,2,3,4,5]
d=4

def rotLeft(a, d):
    return a[d:]+a[:d]
print(rotLeft(a,d))

