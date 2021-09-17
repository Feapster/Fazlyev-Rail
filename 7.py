a = [1, 3, 5, 7, 9, 0]
print(a)
for i in range(len(a)//2):
    c = a[len(a) - 1 - i]
    a[len(a)-1-i] = a[i]
    a[i] = c
print(a)
