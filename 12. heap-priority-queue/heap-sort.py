arr = [5, 4, 3, 2, 1, -1, -89]

def getParentIdx(i):
   return (i - 1) // 2

def getLeftChildIdx(i):
   return (2 * i) + 1

def getRightChildIdx(i):
   return 2 * i + 2

def heapifyDown(arr, i, n):
   left = getLeftChildIdx(i)
   right = getRightChildIdx(i)
   
   greatest = i
   if (left < n and arr[left] > arr[greatest]):
      greatest = left
   
   if (right < n and arr[right] > arr[greatest]):
      greatest = right;
   
   if i != greatest:
      arr[i], arr[greatest] = arr[greatest], arr[i]
      heapifyDown(arr, greatest, n)
   return arr

def heapSort(arr):
   
   for i in range(len(arr), -1, -1):
      heapifyDown(arr, i, len(arr))
   n = len(arr)
   
   for i in range(n):
      arr[n - i - 1],arr[0] = arr[0],arr[n - i - 1]
      heapifyDown(arr, 0, n - i - 1 )
   # for i in range(n - 1, 0, -1):
   #    arr[i],arr[0] = arr[0],arr[i]
   #    heapifyDown(arr, 0, i)
   return arr

heapSort(arr)
print(arr)