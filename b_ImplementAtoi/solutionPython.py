def function(str): 
   num = 0
   flag = 1
   for i in str:
      if i.isnumeric():
         num = num*10+(int(i))
      elif i=='-' or i=='+':
         if i=='-':
            flag = -1
      else:
         break
   if num not in range(float('-inf'),float('inf')):
      return float('inf')*float
   return num * flag
if __name__ == "__main__": 
   t = int(input())
   for _ in range(t):
      str = input()
      print(function(str))


# one test case is being failed