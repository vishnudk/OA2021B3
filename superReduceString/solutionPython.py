s = list(input())
l = len(s)
i = 0
uniq = s[:]
while True:
    l = len(s)
    prv = len(uniq)
    s.clear()
    s = uniq[:]
    uniq.clear()
    while i < l:
        if i+1<l and s[i]==s[i+1]:
            i=i+2
            pass
        else:
            uniq.append(s[i])
            i = i+1
    if prv == len(uniq):
        if len(uniq) == 0:
            print("this string is invalid")
        break
print("".join(uniq))