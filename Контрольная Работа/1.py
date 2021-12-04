n = int(input())
a = [int(input()) for i in range(n)]

r = True

for i in a:
    k = i
    r = True
    while k > 0:
        if k % 10 % 2 != 0:
            r = False
            break
        k = k // 10
    if r:
        print("Есть")
        break

if not r:
    print("Нету")
