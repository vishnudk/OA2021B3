def function(str): 
   if len(str)%2==0:
      stack = []
      for i in str:
         # print(stack)
         if i in list(['(','{','[']):
            stack.append(i)
         elif len(stack)==0:
            return 'NO'
         else:
            tmp = stack.pop()
            if tmp=='(' and i ==')':
               continue
            if (tmp=='[' and i == ']') :
               # print('reached here')
               continue
               # pass
            if tmp=='{' and i=='}':
               continue
            else:
               return 'NO'
      if len(stack)==0:
         return 'YES'
      return 'NO'
   else:
      return "NO"

if __name__ == "__main__": 
   t = int(input())
   for _ in range(t):
      str = list(input())
      print(function(str))
