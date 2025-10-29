# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# T(n): O(n), S(n): O(n)
def isPalindrome(self, s):
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
def isPalindromeStringV2(self, s):
   nstr = ''
   for i in s.lower():
      if i >= 'a' and i <= 'z' or i >= '0' and i <= '9':
            nstr += i
            rev = i + rev
   n = len(nstr)
   for i in range(n//2):
       if (nstr[i] != nstr[n-1-i]):
           return False
   return True

# T(n): O(n), S(n): O(n)
def isPalindromeStringV3(self, s):
   nstr = ''
   rev = ''
   for i in s.lower():
      if i >= 'a' and i <= 'z' or i >= '0' and i <= '9':
            nstr += i
            rev = i + rev
   return rev == nstr
