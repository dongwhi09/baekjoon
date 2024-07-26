n, m = map(int, input().split())
shop = [1000, 1000]
money = 100000
for i in range(m):
    a, b = map(int, input().split())
    if a < shop[0]:
        shop[0] = a
    if b < shop[1]:
        shop[1] = b
if n % 6 == 0:
    if n // 6 * shop[0] < money:
        money = n // 6 * shop[0]
    if n * shop[1] < money:
        money = n * shop[1]
if n % 6 != 0:
    if (n // 6 + 1) * shop[0] < money:
        money = (n // 6 + 1) * shop[0]
    if n * shop[1] < money:
        money = n * shop[1]
    if (n // 6 * shop[0]) + (n % 6 * shop[1]) < money:
        money = (n // 6 * shop[0]) + (n % 6 * shop[1])
print(money)
