a = 'te n!et'
c = 0
for i in range(len(a)//2):
    if not a[i].isalnum() or not a[len(a) - i - 1].isalnum():
        continue
    elif a[i] != a[len(a) - 1 - i]:
        print('Нет')
        c = 1
        break
if c == 0:
    print('Да')
