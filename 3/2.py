from random import randint

a = [4, 17, 1 ,5 ,4]
print(a)

i_1 = 0
i_2 = len(a) - 1
i_m = i_2 - i_1
max = 0
for i in range(len(a) - 1):
    if a[i_1] < a[i_2]:
        i_1 += 1
    else:
        i_2 -= 1
    s = (i_2 - i_1) * (a[i_1] + a[i_2]) * (1/2)
    if s > max:
        max = s
        print(i_2, i_1)

print(max)
