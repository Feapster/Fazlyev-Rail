from random import randint

nums = int(input())

n = randint(0, nums)

a = [[randint(0, nums) for i in range(n)] for j in range(n)]
b = []

for i in range(nums + 1):
    b.append([i, 0])

for i in range(n):
    for j in range(n):
        b[a[i][j]][1] += 1

for i in range(nums + 1):
    print(i, " -", b[i][1], "times")
