# # Complete the makeAnagram function below.
# def makeAnagram(a, b):
#     dels=[]
#     for i in range(len(a)):
#         if a[i] not in b:
#             dels.append(a[i])
#     for j in range(len(b)):
#         if b[j] not in a:
#             dels.append(b[j])
    # return len(dels)

from collections import Counter
def makeAnagram(a, b):
    d1=Counter(a)
    d2=Counter(b)
    result=(d1-d2)+(d2-d1)
    return sum(result.values())
    


# print(number_needed("fcrxzwscanmligyxyvym","jxwtrhvujlmrpdoqbisbwhmgpmeoke"))
print(makeAnagram("fcrxzwscanmligyxyvym","jxwtrhvujlmrpdoqbisbwhmgpmeoke"))