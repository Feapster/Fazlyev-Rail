a = 'автор'
b = 'товар'
d1 = {}

for i in range(len(a)):
    if a[i] in d1:
        d1[a[i]] += 1
    else:
        d1[a[i]] = 1
for i in range(len(a)):
    if b[i] in d1:
        del d1[b[i]]

if d1 == {}:
    print('Да')
else:
    print("Нет")
