# You are given a 0-indexed array of strings words and a character x.
# Return an array of indices representing the words that contain the character x.
# Note that the returned array may be in any order.

# Input: words = ["leet","code"], x = "e"
# Output: [0,1]
# Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

# T(n): O(n * m); S(n): O(1)
def findWordsContainingV1(self, words, x):
   arr = []
   for i in range(len(words)):
      word = words[i]
      if x in word:
         arr.append(i)
   return arr

# T(n): O(n * m); S(n): O(1)
def findWordsContainingV2(self, words, x):
   arr = []
   for i in range(len(words)):
      word = words[i]
      for char in word:
            if x == char:
               arr.append(i)
   return arr
