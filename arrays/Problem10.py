# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# T(n): O(m + n); S(n): O(n + n)
def findMedianSortedArrays(self, nums1, nums2):
   median = (len(nums1) + len(nums2)) // 2
   sorted_arr = [0] * (len(nums1) + len(nums2))
   i = len(nums1) - 1
   j = len(nums2) - 1

   k = len(nums1) + len(nums2) - 1
   while i >= 0 and j >= 0:
      if nums1[i] >= nums2[j]:
            sorted_arr[k] = nums1[i]
            i -= 1
      else:
            sorted_arr[k] = nums2[j]
            j -= 1
      k -= 1
   
   if i >= 0:
      for x in range(i, -1, -1):
            sorted_arr[k] = nums1[x]
            k -= 1
   
   if j >= 0:
      for x in range(j, -1, -1):
            sorted_arr[k] = nums2[x]
            k -= 1
   return sorted_arr[median] if len(sorted_arr) % 2 != 0 else (sorted_arr[median] + sorted_arr[median - 1]) / 2

# T(n): O(log(min(m + n))); S(n): O(1)
def findMedianSortedArrays(nums1, nums2):
      n1 = len(nums1)
      n2 = len(nums2)
      if n1 > n2: return findMedianSortedArrays(nums2, nums1)
      n = n1 + n2
      low = 0
      high = n1
      total = (n1 + n2 + 1) // 2
      while (low <= high):
         mid1 = (low + high) // 2
         mid2 = total - mid1
         l1 = -float('inf')
         l2 = -float('inf')
         r1 = float('inf')
         r2 = float('inf')
         if mid1 - 1 >= 0: l1 = nums1[mid1 - 1]
         if mid2 - 1 >= 0: l2 = nums2[mid2 - 1]
         if mid1 < n1: r1 = nums1[mid1]
         if mid2 < n2: r2 = nums2[mid2]

         if (l1 <= r2 and l2 <= r1):
               if n % 2 == 0:
                  return (max(l1, l2) + min(r1, r2)) / 2
               else:
                  return max(l1, l2)
         elif l1 > r2:
               high = mid1 - 1
         else:
               low = mid1 + 1
      return 0