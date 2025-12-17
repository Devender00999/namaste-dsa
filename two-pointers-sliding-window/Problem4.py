# Index of the First Occurrence in a String
def strStr(self, h: str, n: str) -> int:
   i = 0; 
   for i in range(len(h)):
      j = 0
      if h[i] == n[j]:
            x = i + 1
            y = j + 1
            while x  < len(h) and y < len(n):
               if h[x] != n[y]:
                  break
               x += 1
               y += 1
            if y == len(n):
               return i
   return -1