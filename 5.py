a = [1, 2, 3, 4]
print(a)
a[len(a)-1] += 1
for i in range(len(a)-1, -1, -1):
    if i == 0:
        if a[i] == 10:
            b = [0 for n in range(len(a) + 1)]
            b[0] = 1
            print(b)
        else:
            print(a)
    if a[i] == 10:
        a[i] = 0
        a[i - 1] += 1
