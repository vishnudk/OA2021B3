def function(str,l):
   str = list(str)
   count = 0
   prv = 0
   while prv != l:
      i = 0
      while i < len(str):
         if i+2 < len(str):
            if  str[i]=='x' and str[i+1]=='x' and str[i+2]=='x':
               str.pop(i)
               count = count + 1
               continue
         i = i+1
      prv = l
      l = len(str)
   return count
   
	
if __name__ == "__main__": 
   l = int(input())
   str = input()
   print(function(str,l))
