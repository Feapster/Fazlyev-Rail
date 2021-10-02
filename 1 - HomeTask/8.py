a = 'tenet'
c1, c2 = 1, len(a) - 1

for i in range(len(a)):
    if a[i].isalnum():
        c1 = a[i + 1]
        continue
    if a[len(a) - 1 - i].isalnum():
        c2 = a[i - 1]
        continue
    if a[c1] != a[c2]:
        print(False)
        break

