def function(str , l): 
   max = -1
   for i in str:
      if str.count(i) > max:
         max =  str.count(i)
   if max > len(str)/2:
      return max
   return -1
   
if __name__ == "__main__":
   t = int(input())
   for _ in range(t):
      l = int(input())
      str =  list(input().split() )
      print(function(str , l))
