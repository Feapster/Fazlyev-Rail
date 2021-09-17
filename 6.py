a = [2, 3, 5, 11]
p = 14
print(p)
for i in range(len(a)):
    if p - a[i] in a:
        print(a[i], p - a[i])
        break
