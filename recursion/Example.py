
# print n to 1
def fun(num):
   if num == 0:
      return 
   print(num)
   num = num - 1
   fun(num)
   

# print 1 to n
x = 10 
def fun(n):
   if n > x: return
   print(n)
   n += 1
   fun(n)
   
# print 1 to n
def fun(n):
   if n < 1: return
   fun(n - 1)
   print(n)

fun(10)