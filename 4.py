a = 'автор'
b = 'товар'
c = 0
if len(a) != len(b):
    print('Нет')
else:
    for i in range(len(a)):
        if a.count(a[i]) != b.count(a[i]):
            c = 1
            print('Нет')
            break
if c == 0:
    print('Да')
