n, m = map(int, input().split())
shop = [1001, 1001]
money = 1000000
for i in range(m):
    a, b = map(int, input().split())
    if a < shop[0]:
        shop[0] = a
    if b < shop[1]:
        shop[1] = b
if shop[0] < shop[1] * 6:  
    if shop[0] < (n % 6) * shop[1]:  
        print((n // 6) * shop[0] + shop[0])  
    else:  
        print((n // 6) * shop[0] + (n % 6) * shop[1])  
elif shop[0] >= shop[1] * 6:  
    print(n * shop[1])