a = 'автор'
b = 'товар'
c = 0
for i in range(len(a)):
    if a.count(a[i]) != b.count(a[i]) or len(a) != len(b):
        c = 1
        print('Нет')
        break
if c == 0:
    print('Да')
