# print the following pattern
# 1 2 3 4
# 2 3 4
# 3 4
# 4

for i in range(4):
    print(i + 1, end="")
    for j in range(3 - i):
        print(j + i + 2, end="")

    print()
 