# Check if the number is power of two

def power_of_two(n):
   if (n == 1): 
      return True
   
   if (n % 2 != 0) or n / 2 < 1:
      return False
   
   return power_of_two(n / 2)