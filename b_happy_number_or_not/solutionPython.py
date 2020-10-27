num = list(map(int,input()))
sqr = lambda x: x**2
prv = []
while len(num)>=1:
    num = sum(list(map(sqr,num)))
    num =  [int(i) for i in str(num)]
    if len(num)==1:
        if num[0]==1:
            print("True")
            break
        elif num[0] not in prv:
            prv.append(num[0])
            num.append(0)
        else:
            print("False")
            break
    
