# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
# A substring is a contiguous sequence of characters within a string.

# Input: num = "52"
# Output: "5"
# Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

def largestOddNumber(self, num):
   last_odd = -1
   for i in range(len(num) - 1, -1, -1):
      if int(num[i]) % 2 != 0:
            last_odd = i
            break
   return num[:last_odd + 1] if last_odd != -1 else ""