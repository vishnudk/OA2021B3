s = list(input())
l = len(s)
prv = -1
while l!=prv:
    if prv == -1:
        prv = l
    for i in range(len(s)-1):
        try:
            if s[i] == s[i+1]:
                s.pop(i)
                s.pop(i)
        except:
            pass
    prv = l
    l = len(s)
if len(s)!=0:
    print("".join(s))
else:
    print("Empty String")