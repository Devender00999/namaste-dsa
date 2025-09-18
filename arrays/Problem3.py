# Write a function that reverses a string. The input string is given as an array of characters s.

def reverse(s):
   x = 0
   y = len(s) - 1
   while (x <= y):
      s[x], s[y] = s[y], s[x]
      x += 1
      y -= 1
   print(s)
   
def reverse(s):
   n = len(s)
   for i in range(len(s) // 2):
      s[i], s[n - i - 1] = s[n - i - 1], s[i]
   print(s)
   
reverse(["h","e","l","l","o"])
reverse(["H","a","n","n","a","h"])