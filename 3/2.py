from random import randint

a = [randint(1,9) for i in range(7)]
print(a)

i_1 = 0
i_2 = len(a) - 1
max = (i_2 - i_1) * (a[i_1] + a[i_2]) * (1/2)
for i in range(len(a) - 1):
    if a[i_1] < a[i_2]:
        i_1 += 1
    else:
        i_2 -= 1
    s = (i_1 - i_2) * (a[i_1] + a[i_2]) * (1/2)
    if s > max:
        max = s
print(max)
