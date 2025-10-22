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


def maxFreqSum(self, s):
   v = set(['a', 'e', 'i', 'o', 'u'])
   c = set(['b', 'c', 'd', 'f','g','h','j', 'k', 'l','m', 'n','p','q','r','s','t','v','w','x','y','z'])
   vowels = {}
   consonants = {}
   for i in list(s):
      if i in v:
            if vowels.get(i):
               vowels[i] = vowels.get(i) + 1
            else:
               vowels[i] = 1
      
      if i in c:
            if consonants.get(i):
               consonants[i] = consonants.get(i) + 1
            else:
               consonants[i] = 1
   return max(vowels.values() or [0]) + max(consonants.values() or [0])
      

   