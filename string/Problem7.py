# Reverse a string with start and end.
def reverse(s, start, end):
   length = len(s)
   if start < 0 or end >= length: return s
   rev = ''
   if start > 0:
      rev += s[:start ]
   for i in range(end, start - 1, -1):
      rev += s[i]
   if end < len(s):
      rev += s[end + 1: len(s)]
   return rev

def reverseStr(self, s, k):
   start = 0
   l = len(s)
   while start < l:
      if len(s[start: l]) >= k:
            s = self.reverse(s, start, start + k - 1)
      else:
            s = self.reverse(s, start, l - 1)
      start = start + (2 * k)
   return s

def reverseStr(s, k):
   n = len(s)
   slist = list(s)
   for x in range(0, n, k * 2):   
      for i in range(k // 2):
         slist[x + i], slist[x + k - 1 - i] = slist[x + k - 1 - i], slist[x + i] 
   return "".join(slist)
print(reverseStr('abcdefg', 2))