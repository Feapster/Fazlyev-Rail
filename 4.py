a, b = 'автор', 'товар'
d1 = {}
d2 = {}

for i in range(len(a)):
    if a[i] in d1:
        d1[a[i]] += 1
    else:
        d1[a[i]] = 1
    if b[i] in d2:
        d2[b[i]] += 1
    else:
        d2[b[i]] = 1

print(d1 == d2)
