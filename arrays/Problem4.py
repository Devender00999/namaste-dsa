# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maximum_profit(arr):
   x = 0
   profit = 0
   for i in range(0, len(arr)):
      if arr[i] < arr[x]:
         x = i
      currProfit = arr[i] - arr[x]
      if currProfit > profit:
         profit = currProfit
   return profit

print(maximum_profit([7,1,5,3,6,4]))
print(maximum_profit([7,6,4,3,1]))
         
         