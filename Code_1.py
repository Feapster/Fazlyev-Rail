# 0
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

# 1

a = [9, 9, 9, 8]
print(a) 
a[len(a)-1] += 1 
for i in range(len(a)-1, -1, -1): 
    if i == 0: 
        if a[i] == 10: 
            b = [0 for n in range(len(a) + 1)] 
            b[0] = 1 
            print(b) 
        else: 
            print(a) 
    if a[i] == 10: 
        a[i] = 0 
        a[i - 1] += 1

# 2

a = [2, 3, 5, 11]
p = 14
print(p)
for i in range(len(a)): 
    if p - a[i] in a: 
        print(a[i], p - a[i]) 
        break

# 3

a = [1, 3, 5, 7, 9, 0] 
print(a) 
for i in range(len(a)//2): 
    c = a[len(a) - 1 - i] 
    a[len(a)-1-i] = a[i] 
    a[i] = c 
print(a)

# 4

a = 'tenet' 
c = 0 
for i in range(len(a)//2): 
    if a[i] != a[len(a) - 1 - i]: 
        print('Нет') 
        c = 1 
        break 
if c == 0: 
    print('Да')
