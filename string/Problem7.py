# Palindrome
def isPalindrome(self, s):
   """
   :type s: str
   :rtype: bool
   """
   nstr = ''
   for i in s.lower():
      if i >= 'a' and i <= 'z' or i >= '0' and i <= '9':
            nstr += i
   print(nstr)
   return nstr == nstr[::-1]
