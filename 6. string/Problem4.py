# You are given a string s consisting of lowercase English letters ('a' to 'z').
# Your task is to:
# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.

# Input: s = "successes"
# Output: 6

# Explanation:
# The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
# The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
# The output is 2 + 4 = 6.


def maxFreqSum(s):
   v = set(['a', 'e', 'i', 'o', 'u']) 
   vowels = {}
   consonants = {}
   for i in list(s):
      if i in v:
            if vowels.get(i):
               vowels[i] = vowels.get(i) + 1
            else:
               vowels[i] = 1
      else:
            if consonants.get(i):
               consonants[i] = consonants.get(i) + 1
            else:
               consonants[i] = 1
   return max(vowels.values() or [0]) + max(consonants.values() or [0])
      

   