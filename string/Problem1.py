# Given a string s consisting of words and spaces, return the length of the last word in the string.
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# T(n): O(n); S(n): O(1)
def lengthOfLastWord(s):
   count = 0
   isWord = False
   for i in range(len(s) - 1, -1, -1):
      if s[i] != ' ':
            count += 1
            isWord = True
      if isWord and s[i] == ' ':
            break
   return count

# T(n): O(n); S(n): O(1)
def lengthOfLastWordV2(s):
   n = len(s) -  1
   while s[n] == ' ':
      n -= 1
   count = 0
   for i in range(n, -1, -1):
      if s[i] == ' ':
         break
      count += 1
   return count

