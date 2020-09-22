import string

x = input('Enter 1st name')
y = input('Enter 2nd name')

print(y + " " + x)

values = input('Enter some coma separated values')
list = values.split(",")  # split values with comma
tuple = tuple(list)
print('List=', list)
print('Tuple=', tuple)

file = input("enter file with extension")
f_ext = file.split(".")
print('Extension is' + repr(f_ext[-1]))
