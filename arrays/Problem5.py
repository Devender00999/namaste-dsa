# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# i/p: [1,2,3,0,0,0], 3, [2,5,6], 3
# o/p: [1, 2, 2, 3, 5, 6]


# T(n): O(m + n), S(n): O(m)
def merge_sorted_array(nums1, m, nums2, n):
   temp_n1 = []
   for i in range(m):
      temp_n1.append(nums1[i])
   p1 = 0
   p2 = 0
   for i in range(m + n):
      if p1 < m and p2 < n:
         if temp_n1[p1] <= nums2[p2]:
            nums1[i] = temp_n1[p1]
            p1 += 1
         else:
            nums1[i] = nums2[p2]
            p2 += 1
      else:
         if p1 < m:
            nums1[i] = temp_n1[p1]
            p1 += 1
         if p2 < n:
            nums1[i] = nums2[p2]
            p2 += 1
   return nums1     

# T(n): O(m + n), S(n): O(m)
def merge_sorted_array(nums1, m, nums2, n):
   temp_n1 = []
   for i in range(m):
      temp_n1.append(nums1[i])
   p1 = 0
   p2 = 0
   for i in range(m + n):
      if p2 >= n or (p1 < m and temp_n1[p1] <= nums2[p2]):
         nums1[i] = temp_n1[p1]
         p1 += 1
      else:
         nums1[i] = nums2[p2]
         p2 += 1
      
   return nums1     

def merge_sorted_array(nums1, m, nums2, n):
   p1 = m - 1
   p2 = n - 1
   for i in range(m + n - 1, -1, -1):
      if p2 < 0: break
      
      if p1 >= 0 and nums1[p1] > nums2[p2]:
         nums1[i] = nums1[p1]
         p1-= 1
      else:
         nums1[i] = nums2[p2]
         p2 -= 1
   return nums1     

print(merge_sorted_array([1,2,3,0,0,0], 3, [2,5,6], 3))
print(merge_sorted_array([1], 1, [0], 0))
