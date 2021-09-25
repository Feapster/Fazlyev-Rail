a = 'te n!et'
s = "!$%&'()*+,-./:;<=>?@[]^_`{|}~# "
c = 0
for i in range(len(a)//2):
    if a[i] != a[len(a) - 1 - i] and a[i] not in s:
        print('Нет')
        c = 1
        break
if c == 0:
    print('Да')
