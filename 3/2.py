from random import randint

a = [randint(1,10) for i in range(12)]
print(a)
max_0 = 0
for i in range(len(a)):
    for j in range(len(a)):
        min_1 = min(a[i], a[j])
        max_1 = max(a[i], a[j])
        s = (i - j) * (min_1 + (max_1 - min_1)*(1/2))
        if max_0 < s:
            max_0 = s
print(max_0)
