from array import *

arr = array('i', [])

n = int(input("Enter length of array"))

for i in range(n):
    y = int(input("Enter next value"))
    arr.append(y)

print(arr)
