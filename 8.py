a = 'tenet'
c = 0
for i in range(len(a)//2):
    if a[i] != a[len(a) - 1 - i]:
        print('Нет')
        c = 1
        break
if c == 0:
    print('Да')
