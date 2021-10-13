# Python program to add two binary numbers.

# Driver code
# Declaring the variables
a = "1101"
b = "100"

# Calculating binary value using function
sum = bin(int(a, 2) + int(b, 2))

# Printing result
print(sum[2:])
