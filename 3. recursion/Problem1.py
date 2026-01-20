# sum of n numbers using recursion

# T(n): O(n), S(n): O(n)
def find_sum(n):
   if n == 1: return 1
   sum = find_sum(n - 1)
   return n + sum

print(find_sum(5))