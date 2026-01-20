# fibonacci number
# f(0) = 0, f(1)= 1, f(n) = f(n - 1) + f(n - 2)

def fib(n):
   if n <= 1: return n
   return fib(n - 1) + fib(n - 2)

print(fib(6))