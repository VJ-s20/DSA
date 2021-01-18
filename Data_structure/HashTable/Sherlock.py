from collections import Counter

def sherlockAndAnagrams(s):
    # d=Counter(s)
    # print(d)
    collect=[]
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            collect.append(s[i:i+j])

    print(collect)

sherlockAndAnagrams("kkkk")
    