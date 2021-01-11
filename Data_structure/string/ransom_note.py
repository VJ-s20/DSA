# from collections import Counter
# def checkMagazine(magazine, note):
#     mag=Counter(magazine)
#     notes=Counter(note)
#     if mag

# print(checkMagazine("give me one grand today night","give one grand today"))  


def repeatedString(s, n):
    if len(s)==1:
        return n
    letters=[]

    while len(letters)<n:
        for i in s:
            letters.append(i)

    return letters


print(repeatedString("aba",10))