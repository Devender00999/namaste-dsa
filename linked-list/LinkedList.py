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
   
   

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtTail(1)
obj.addAtTail(2)
obj.addAtTail(3)
obj.addAtTail(4)
obj.addAtTail(5)
obj.addAtTail(6)
obj.addAtTail(7)
obj.addAtTail(8)
obj.addAtTail(9)

def print_linked_list(head: Node):
   curr = head
   while curr != None:
      print(curr.val, end=" ")
      curr = curr.next
   print()
   
# print_linked_list(obj.middleNode(obj.head))

print_linked_list(obj.head)
obj.reverse_list(obj.head)
print_linked_list(obj.head)


# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)