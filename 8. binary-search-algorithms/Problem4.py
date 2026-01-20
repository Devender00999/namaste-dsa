# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Input: n = 5, bad = 4
# Output: 4

def isBadVersion():
   return 2

# T(n): O(log(n))
def firstBadVersion(self, n: int) -> int:
   l = 1
   r = n
   while l <= r:
       m = l + (r - l) // 2
       if isBadVersion(m):
           r = m
       else:
           if isBadVersion(m + 1):
               return m + 1
           else:
               l = m + 1
   return -1
   
# T(n): O(log(n))
def firstBadVersion(n):
   while l < r:
      m = l + (r - l) // 2
      if not isBadVersion(m):
            l = m + 1
      else:
            r = m
   return r