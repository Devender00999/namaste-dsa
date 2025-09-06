#  * * * * 
#  * * * * 
#  * * * * 
#  * * * * 
n = 5
for i in range(n):
   for j in range(n):
      print(" *", end="")
   print('')
print()
   
#  * * * * 
#  * * * * 
#  * * * * 
#  * * * * 
for i in range(n):
   row = " "
   for j in range(n):
      row = row + "* "
   print(row)
print()

#  * 
#  * * 
#  * * * 
#  * * * *
for i in range(n):
   row = " "
   for j in range(i + 1):
      row += "* "
   print(row)
print()

#  1 
#  1 2 
#  1 2 3 
#  1 2 3 4
for i in range(n):
   row = " "
   for j in range(i + 1):
      row += str(j + 1) + " "
   print(row)
print()

#  1 
#  2 2 
#  3 3 3 
#  4 4 4 4 
for i in range(n):
   row = " "
   for j in range(i + 1):
      row += str(i + 1) + " "
   print(row)
print()

#  1 2 3 4 5 
#  1 2 3 4 
#  1 2 3 
#  1 2 
#  1 
for i in range(n):
   row = " "
   for j in range(n - i):
      row = row + str(j + 1) + " "
   print(row)
print()

#  * * * * * 
#  * * * * 
#  * * * 
#  * * 
#  *    
for i in range(n):
   row = " "
   for j in range(n - i):
      row = row + "* "
   print(row)
print()

#          * 
#        * * 
#      * * * 
#    * * * * 
#  * * * * * 
for i in range(n):
   row = " "
   for j in range(n - (i + 1)):
      row = row + "  "
   for j in range(i + 1):
      row = row + "* "
   print(row)
print()

#  1  
#  1  0 
#  1  0 1  
#  1  0 1  0 
#  1  0 1  0 1
for i in range(n): 
   row = " "
   for j in range(i + 1):
      if j % 2 == 0:
         row = row + "1  "
      else:
         row = row + "0 "
   print(row)
print()

#  1 
#  1 0 
#  1 0 1 
#  1 0 1 0 
#  1 0 1 0 1 
for i in range(n): 
   row = " "
   switch = '1'
   for j in range(i + 1):
      row = row + switch + ' '
      if switch == '0':
         switch = "1"
      else:
         switch = "0"
   print(row)
print()

#  1 
#  0 1 
#  0 1 0 
#  1 0 1 0 
#  1 0 1 0 1
switch = '1'
for i in range(n): 
   row = " "
   for j in range(i + 1):
      row = row + switch + ' '
      if switch == '0':
         switch = "1"
      else:
         switch = "0"
   print(row)

