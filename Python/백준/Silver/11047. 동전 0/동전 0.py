n, k = map(int, input().split())
coin, x = [], 0
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
for i in range(len(coin)):
    x += k // coin[i]
    k = k % coin[i]
print(x)