# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# T(n): O(n), S(n): O(n)
def isPalindromeString(s):
   """
   :type s: str
   :rtype: bool
   """
   nstr = ''
   for i in s.lower():
      if i >= 'a' and i <= 'z' or i >= '0' and i <= '9':
            nstr += i
   return nstr == nstr[::-1]

# T(n): O(n), S(n): O(n)
def isPalindromeStringV2(s):
   nstr = ''
   for i in s.lower():
      if i >= 'a' and i <= 'z' or i >= '0' and i <= '9':
            nstr += i
   n = len(nstr)
   for i in range(n//2):
       if (nstr[i] != nstr[n-1-i]):
           return False
   return True

# T(n): O(n), S(n): O(n)
def isPalindromeStringV3(s):
   nstr = ''
   rev = ''
   for i in s.lower():
      if i >= 'a' and i <= 'z' or i >= '0' and i <= '9':
            nstr += i
            rev = i + rev
   return rev == nstr

def isAlphaNum(i):
      return i >= 'a' and i <= 'z' or i >= '0' and i <= '9'

# T(n): O(n), S(n): O(1)
def isPalindromeStringV4(s):
   start = 0
   end = len(s) - 1
   s = s.lower()
   while start < end:
      if not isAlphaNum(s[start]):
         start += 1
      elif not isAlphaNum(s[end]):
         end -= 1
      elif s[start] == s[end]:
         start += 1
         end -= 1
      else:
         return False
   return True

print(isPalindromeStringV4('A man, a plan, a canal: Panama'))
# print(isPalindromeString('A man, a plan, a canal: Panama'))
# print(isPalindromeStringV2('A man, a plan, a canal: Panama'))
# print(isPalindromeStringV3('A man, a plan, a canal: Panama'))