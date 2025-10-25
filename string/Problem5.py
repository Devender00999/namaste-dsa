# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it into some number of substrings such that:
# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# T(n): O(n); S(n): O(1)
def balancedStringSplit(s):
   balancedCount = 0
   countL = 0
   countR = 0
   for i in s:
      
       if i == 'L':
           countL += 1
      
       if i == 'R':
           countR += 1
      
       if countL == countR:
           balancedCount += 1
           countL = 0
           countR = 0
   return balancedCount

# T(n): O(n); S(n): O(1)
def balancedStringSplitV2(s):
   count = 0
   count_lr = 0
   for i in s:
      if i == 'L':
            count_lr += 1
      else:
            count_lr -= 1

      if count_lr == 0:
            count += 1
   return count