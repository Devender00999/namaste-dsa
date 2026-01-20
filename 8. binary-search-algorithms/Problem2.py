# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# Input: n = 10, pick = 6
# Output: 6

# T(n): O(logn); S(n): O(1)
def guessNumber(self, n: int) -> int:
   l = 1
   r = n
   while l <= r:
      mid = l + (r - l) // 2
      print(mid)
      num = guess(mid)
      if (num == 0):
            return mid
      elif num == -1:
            r = mid - 1
      else:
            l = mid + 1
   return 0
