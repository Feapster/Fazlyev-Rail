a = [1, 3, 3, 4, 6, 7]
b = [4, 4, 6, 7]

print(a)
print(b)

res = []

i_1 = 0
i_2 = 0

for i in range(len(a) + len(b)):
    if i_1 == len(a) and i_2 == len(b):
        break
    elif i_1 == len(a):
        res.append(b[i_2])
        i_2 += 1
        continue
    elif i_2 == len(b):
        res.append(a[i_1])
        i_1 += 1
        continue
    if i_1 != len(a) and a[i_1] < b[i_2]:
        res.append(a[i_1])
        i_1 += 1
    elif a[i_1] > b[i_2]:
        res.append(b[i_2])
        i_2 += 1
    else:
        res.append(a[i_1])
        res.append(b[i_2])
        i_1 += 1
        i_2 += 1

print(res)
