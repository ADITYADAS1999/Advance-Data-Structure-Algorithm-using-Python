# Python program to merge two unsorted lists 
# in sorted order
# Function to merge array in sorted order
def unsortedarray (a, b, res, n, m):
   # Sorting a[] and b[]
   a.sort()
   b.sort()
   # Merge two sorted arrays into res[]
   i, j, k = 0, 0, 0
   while (i < n and j < m):
      if (a[i] <= b[j]):
         res[k] = a[i]
         i += 1
         k += 1
      else:
         res[k] = b[j]
         j += 1
         k += 1
   while (i < n):  # Merging remaining
      # elements of a[] (if any)
      res[k] = a[i]
      i += 1
      k += 1
   while (j < m):  # Merging remaining
      # elements of b[] (if any)
      res[k] = b[j]
      j += 1
      k += 1
# Driver code
A=list()
n=int(input("Enter the size of the First List ::"))
print("Enter the Element of First List ::")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
B=list()
m=int(input("Enter the size of the Second List ::"))
print("Enter the Element of Second List ::")
for i in range(int(n)):
   k=int(input(""))
   B.append(k)
# Final merge list
res = [0 for i in range(n + m)]
unsortedarray(A, B, res, n, m)
print ("Sorted merged list :")
for i in range(n + m):
   print (res[i],)
