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
def number_needed(a, b):
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return ct_a,(ct_a-ct_b)


print(number_needed("fcrxzwscanmligyxyvym","jxwtrhvujlmrpdoqbisbwhmgpmeoke"))
# print(makeAnagram("fcrxzwscanmligyxyvym","jxwtrhvujlmrpdoqbisbwhmgpmeoke"))