"""
"""

from collections import Counter
def checkMagazine(magazine, note):
    d1=Counter(magazine)
    d2=Counter(note)
    d3=d2-d1
    if sum(d3.values())==0:
        print("Yes")
    else:
        print("No")
def checkMagazine(magazine, note):
    magazine=magazine.split()
    note=note.split()
    for i in magazine:
        if i in note:
            note.remove(i)
    print(note)


checkMagazine("two times three is not four","two times two is four")
# checkMagazine("give me one grand today night","give one grand today")