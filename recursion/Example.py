
def fun(num):
   if num == 0:
      return 
   print(num)
   num = num - 1
   fun(num)

fun(5)