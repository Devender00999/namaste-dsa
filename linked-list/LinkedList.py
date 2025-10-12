class Node():
   def __init__(self, val):
      self.val = val
      self.next = None

class MyLinkedList(object):
   def __init__(self):
      self.head = None
      self.size = 0

   def get(self, index):
      
      """
      :type index: int
      :rtype: int
      """
      if index < 0 or index >= self.size:
         return -1
      curr = self.head
      for i in range(index):
         curr = curr.next
      return curr.val
      

   def addAtHead(self, val):
      """
      :type val: int
      :rtype: None
      """
      new_node = Node(val)
      new_node.next = self.head
      self.head = new_node
      self.size += 1
      

   def addAtTail(self, val):
      """
      :type val: int
      :rtype: None
      """
      node = Node(val)
      if self.head == None:
         self.head = node
         self.size += 1
         return           

      curr = self.head 
      while curr.next != None:
         curr = curr.next
      curr.next = node
      self.size += 1
      

   def addAtIndex(self, index, val):
      """
      :type index: int
      :type val: int
      :rtype: None
      """
      if index < 0 or index > self.size:
         return
      if index == 0:
         self.addAtHead(val)
      elif index == self.size:
         self.addAtTail(val)
      else:
         node = Node(val)
         curr = self.head
         # for i in range(index - 1):
         #     curr = curr.next
         while index > 1:
               curr = curr.next
               index -= 1
         node.next = curr.next
         curr.next = node    
         self.size += 1        
      

   def deleteAtIndex(self, index):
      """
      :type index: int
      :rtype: None
      """
      if index < 0 or index >= self.size:
         return
      if index == 0:
         self.head = self.head.next
      else:
         curr = self.head
         for i in range(index - 1):
               curr = curr.next 
         curr.next = curr.next.next
      self.size -= 1
        
   # T(n): O(n), S(n): O(1)
   def middleNode(self, head):
      slow = head 
      fast = head
      while fast != None and fast.next != None:
         slow = slow.next
         fast = fast.next.next
      return slow
   
   # T(n): O(n), S(n): O(n)
   def middle_node(self, head):
      arr = []
      curr = head
      while curr.next != None:
         arr.append(curr.val)
         curr = curr.next
      middle = len(arr) // 2

      curr = self.head
      for i in range(middle):
         curr = curr.next
         
      if len(arr) % 2 != 0:
         curr = curr.next
      return curr
   
   def reverse_list(self, head):
      prev = None
      curr = head
      while curr:
         temp = curr.next
         curr.next = prev
         prev = curr
         curr = temp
      self.head = prev
      
   # T(n): O(n); S(n): O(n)
   def hasCycleV2(self, head):
      li = set()
      curr = head
      while curr:
         if curr in li:
               return True
         li.add(curr)
         curr = curr.next
      return False
   
   # T(n): O(n); S(n): O(1)
   def hasCycle(self, head):
      slow = head
      fast = head
      while fast and fast.next:
         slow = slow.next
         fast = fast.next.next
         if slow == fast:
               return True
      return False
   
   # T(n): O(n); S(n): O(n)
   def isPalindrome(self, head):
      li = []
      curr = head
      while curr:
         li.append(curr.val)
         curr = curr.next
      n = len(li)
      for i in range(len(li) // 2):
         if li[i] != li[n - i - 1]:
               return False
      return True

   def print_linked_list(self, head: Node):
      curr = head
      while curr != None:
         print(curr.val, end=" ")
         curr = curr.next
      print()
   
   def isPalindromeV2(self, head):
      # find middle of the linked list
      slow = head
      fast = head
      while fast and fast.next:
         slow = slow.next
         fast = fast.next.next
      
      # reversing the second half of the list
      curr = slow
      prev = None
      while curr:
         temp = curr.next
         curr.next = prev
         prev = curr
         curr = temp
      slow = prev
      
      # comparing first half and second half
      curr = slow
      curr1 = head
      while curr:
         if curr.val != curr1.val:
            curr = slow
            prev = None
            while curr:
               temp = curr.next
               curr.next = prev
               prev = curr
               curr = temp
            slow = prev
            return False
         curr = curr.next
         curr1 = curr1.next
         
      curr = slow
      prev = None
      while curr:
         temp = curr.next
         curr.next = prev
         prev = curr
         curr = temp
      slow = prev
      
      return True
   
   # T(n): O(n * m); S(n): O(1)
   def getIntersectionNode(self, headA, headB):
      """
      :type head1, head1: ListNode
      :rtype: ListNode
      """
      curr = headA
      while curr:
            curr2 = headB
            while curr2:
               if curr == curr2:
                  return curr
               curr2 = curr2.next
            curr = curr.next
      return None
   
   # T(n): O(n + m); S(n): O(n)
   def getIntersectionNode(self, headA, headB):
      """
      :type head1, head1: ListNode
      :rtype: ListNode
      """
      curr = headA
      while curr.next:
         curr2 = headB
         while curr2:
            if curr == curr2:
               return curr
            curr2 = curr2.next
            
         curr = curr.next
      return None
   
   # T(n): O(n + m); S(n): O(n)
   def getIntersectionNode(self, headA, headB):
      """
      :type head1, head1: ListNode
      :rtype: ListNode
      """
      s = set()
      curr = headA
      while curr.next:
         s.add(curr)
         curr = curr.next
      last = curr
      curr = headB
      while curr:
         if last == curr:
               return curr
         curr = curr.next
         
         
   # Given the head of a linked list and an integer val, 
   # remove all the nodes of the linked list that has Node.val == val, and return the new head.
   # T(n): O(n); S(n): O(1)
   def removeAllOccuranceOfElement(self, head, val):
      prev = None
      curr = head
      while curr:
         if curr.val == val:
               print('Hi')
               if prev is None:
                  head = curr.next
               else:
                  prev.next = curr.next
         else:
               prev = curr
         curr = curr.next
      return head

   # T(n): O(n); S(n): O(1)
   def removeAllOccuranceOfElementV2(self, head, val):
      sentiel = Node(0)
      sentiel.next = head
      prev = sentiel
      while prev and prev.next:
          if prev.next.val == val:
              prev.next = prev.next.next
          else:
              prev = prev.next
      return sentiel.next
   
   # Given the head of a linked list, remove the nth node from the end of the list and return its head.
   # T(n): O(n); S(n): O(1)
   def removeNthFromEnd(self, head, n):
      """
      :type head: Optional[ListNode]
      :type n: int
      :rtype: Optional[ListNode]
      """
      if n < 1:
         return head
      x = 0
      curr =head
      while curr:
         x += 1
         curr = curr.next
      
      curr = head
      j = 0
      if n == x:
         head = head.next
         return head
      while curr and j < x - n - 1:
         j += 1
         curr = curr.next
      if curr.next:
         curr.next = curr.next.next
      else:
         head = head.next
      return head
   
   # T(n): O(n); S(n): O(1) (Two Pass)
   def removeNthFromEndV2(self, head, n):
      sentinel = Node(0)
      sentinel.next = head
      
      length = 0
      curr = head
      while curr:
         curr = curr.next
         length += 1
      
      prev = sentinel
      prevPos = length - n
      for i in range(prevPos):
         prev = prev.next
      prev.next = prev.next.next
      return sentinel.next

   # T(n): O(n); S(n): O(1) (One Pass)
   def removeNthFromEndV2(self, head, n):
      sentinel = Node(0)
      sentinel.next = head
      
      first = sentinel
      second = sentinel

      for i in range(n):
         second = second.next
      
      while second and second.next:
         first = first.next
         second = second.next
      
      first.next = first.next.next
      return sentinel.next

   # T(n): O(n): S(n): O(1)
   def deleteDuplicates(self, head):
      """
      :type head: Optional[ListNode]
      :rtype: Optional[ListNode]
      """
      curr = head
      while curr and curr.next:
         # Approach 1
         if curr.val == curr.next.val:
            curr.next = curr.next.next
         else:
            curr = curr.next

      # Approach 2
      # curr = head
      # prev = head
      # while curr and curr.next:
      #    if prev.val != curr.next.val:
      #          prev.next = curr.next
      #          prev = curr.next
      #    curr = curr.next
      # if prev and prev.next:
      #    prev.next = None
      # return head
   
   # Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
   # T(n): O(n), S(n): O(n)
   def oddEvenList(self, head):
      """
      :type head: Optional[ListNode]
      :rtype: Optional[ListNode]
      """
      if not head or not head.next: return head
      odd = head
      even = head.next
      evenStart = even
      
      while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
      
      odd.next = evenStart
      return head
   
   # You are given two non-empty linked lists representing two non-negative integers. 
   # The digits are stored in reverse order, and each of their nodes contains a single digit. 
   # Add the two numbers and return the sum as a linked list.

   def addTwoNumbers(self, l1, l2):
      """
      :type l1: Optional[ListNode]
      :type l2: Optional[ListNode]
      :rtype: Optional[ListNode]
      """
      carry = 0
      curr1 = l1
      curr2 = l2
      head = None
      li = head
      while curr1 and curr2:
         s = curr1.val + curr2.val + carry
         carry = 1 if s > 9 else 0
         node = Node(s % 10)
         if not head:
               head = node
               li = node
         else:
               li.next = node
               li = li.next
         curr1 = curr1.next
         curr2 = curr2.next
      curr1 = curr1 or curr2         
      while curr1: 
         s = curr1.val + carry
         carry = 1 if s > 9 else 0
         node = Node(s % 10)
         li.next = node
         li = li.next
         curr1 = curr1.next
      if carry:
         node = Node(carry)
         li.next = node
      return head

   def addTwoNumbers(self, l1, l2):
      """
      :type l1: Optional[ListNode]
      :type l2: Optional[ListNode]
      :rtype: Optional[ListNode]
      """
      carry = 0
      ans = Node(0)
      head = ans
      while l1 or l2 or carry:
         currentSum = carry
         if l1:
               currentSum += l1.val
               l1 = l1.next
         if l2:
               currentSum += l2.val
               l2 = l2.next
         carry = currentSum // 10
         
         node = Node(currentSum % 10)
         ans.next = node
         ans = ans.next

      return head.next

   

   

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtTail(1)
obj.addAtTail(2)
obj.addAtTail(3)
obj.addAtTail(4)
obj.addAtTail(5)

def print_linked_list(head: Node):
   curr = head
   while curr != None:
      print(curr.val, end=" ")
      curr = curr.next
   print()
   
# print_linked_list(obj.middleNode(obj.head))

# obj.reverse_list(obj.head)
print_linked_list(obj.head)
print(print_linked_list(obj.removeNthFromEnd(obj.head, 0)))
# obj.print_linked_list(obj.head)
# obj.removeElementsV2(obj.head, 1)

# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)