n, k = map(int, input().split())
coin, x = [], 0
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
print(coin)
while k != 0:
    for i in range(len(coin)):
        k = k % coin[i]
        x += k // coin[i]
print(x)