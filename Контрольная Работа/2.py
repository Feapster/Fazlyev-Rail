n = int(input())
x = int(input())

answer = 0

factorial = 1
znak = 1
verh = x

for k in range(1, n+1):
    znak *= -1
    verh *= x**2
    factorial *= k
    num = (znak * verh) / (factorial + x)
    answer += num

print(answer)
