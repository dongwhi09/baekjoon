n = int(input())
x = 0
while n != 0:
    if n % 5 == 0:
        x += (n // 5)
        print(x)
        break
    if n % 5 != 0:
        n = n - 3
        x += 1
    if n == 0:
        print(x)
        break
    if n < 0:
        print(-1)
        break