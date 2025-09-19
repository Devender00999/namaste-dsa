# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

def merge_sorted_array(nums1, m, nums2, n):
   temp_n1 = []
   for i in range(m):
      temp_n1.append(nums1[i])

   p1 = 0
   p2 = 0
   for i in range(m + n):
      if (p1 < m and p2 < n):
         if temp_n1[p1] > nums2[p2]:
            if (p1 < m):
               nums1[i] = nums2[p2]
               p2 += 1
         else:
            nums1[i] = temp_n1[p1]
            p1 += 1
   return nums1     
print(merge_sorted_array([1,2,3,0,0,0], 3, [2,5,6], 3))
   