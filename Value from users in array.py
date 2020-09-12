from array import *

arr = array('i', [])

n = int(input("Enter length of array"))

for i in range(n):
    y = int(input("Enter next value"))
    arr.append(y)

print(arr)

z = int(input("Enter number to be searched in array"))
k = 0
for e in arr:
    if e == z:
        print("Index number of searched no. in array is", k)
        break
    k + 1
else:
    print("Searched no not in array")

# print(arr.index(z))
