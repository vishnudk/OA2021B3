def function(n,k): 
	 num = [int(i) for i in str(n)]
    num = [int(i) for i in str(sum(num)*k)]
    while len(num)>1:
        num = [int(i) for i in str(sum(num))]
    return sum(num)
if __name__ == "__main__": 
   n= int(input())
   k= int(input())
   print(function(n,k))
