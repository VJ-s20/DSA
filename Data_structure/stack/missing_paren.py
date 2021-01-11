# Problem 1 
# from stack import Stack
# def matching(p1,p2):
#     if p1=="(" and p2==")":
#         return True
#     elif p1=="[" and p2=="]":
#         return True
#     elif p1=="{" and p2=="}":
#         return True
#     else:
#         return False
# def balaced_par(paras):
#     s=Stack()
#     is_balaced=True
#     index =0
#     while index<len(paras) and is_balaced:
#         para=paras[index]
#         if para in "({[":
#             s.push(para)
#         else:
#             if s.is_empty():
#                 is_balaced=False
#             else:
#                 top=s.pop()
#                 if not matching(top,para):
#                     is_balaced=False
#         index+=1
#     if s.is_empty() and is_balaced:
#         return True
#     else:
#         return False

# b=balaced_par("([{}]]")
# print(b)



from stack import Stack

def is_match(p1,p2):
    if p1=="(" and p2==")":
        return True
    elif p1=="{" and p2=="}":
        return True
    elif p1=="[" and p2=="]":
        return True
    return False
def missing_paren(string):
    s=Stack()
    for i in range(len(string)):
        paren=string[i]
        if paren in "[{(":
            s.push(paren)
        else:
            if s.is_empty():
                return False
            else:
                top=s.pop()
                if not is_match(top,paren):
                    return False
                
    if s.is_empty():
        return True

print(missing_paren("([[]]})}"))
