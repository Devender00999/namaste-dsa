# Index of the First Occurrence in a String

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0

# T(n): O(n*m); S(n): O(1)
def strStr(self, haystack: str, needle: str) -> int:
   i = 0; 
   for i in range(len(haystack)):
      j = 0
      if haystack[i] == needle[j]:
            x = i + 1
            y = j + 1
            while x  < len(haystack) and y < len(needle):
               if haystack[x] != needle[y]:
                  break
               x += 1
               y += 1
            if y == len(needle):
               return i
   return -1
  
# T(n): O(n*m); S(n): O(1)
def strStr(haystack: str, needle: str) -> int:
   m, n = len(haystack), len(needle)
   for i in range(m - n + 1):
      j = 0
      while j < n:
            if haystack[i + j] != needle[j]:
               break
            j += 1
      if j == n:
            return i
   return -1

# KMP algorithm