# Reverse a string with start and end.
def reverse(s, start, end):
   length = len(s)
   if start < 0 or end >= length: return s
   rev = ''
   if start > 0:
      rev += s[:start ]
   for i in range(end, start - 1, -1):
      print(i)
      rev += s[i]
   if end < len(s):
      rev += s[end + 1: len(s)]
   return rev


print(reverse('hello', 1, 3))