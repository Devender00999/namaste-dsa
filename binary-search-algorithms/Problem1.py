# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
# The returned integer should be non-negative as well.

# Input: x = 4
# Output: 2

# T(n): O(logn); S(n): O(1)
def mySqrt(self, x: int) -> int:
   if x < 2: return x
   l = 2
   r = x // 2
   while l <= r:
      m = (l + r) // 2
      if x == m * m: return m
      elif x > m * m:
            l = m + 1
      else:
            r = m - 1
   return r

# T(n): O(n); S(n): O(1)
def mySqrt(x: int) -> int:
   if x == 1 or x == 2: return 1
   for i in range(1, x):
       if i * i > x:
           return i - 1
   return 0