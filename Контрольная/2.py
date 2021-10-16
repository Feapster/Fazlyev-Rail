from random import randint

a = [randint(0,7) for i in range(8)]

b = []

print(a)

for j in range(3):
    max = 0
    for i in range(len(a)):
        if a[i] >= max and a[i] not in b:
            max = a[i]
    b.append(max)
print(b[2])
