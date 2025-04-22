n = int(input())
n = list(bin(n)[2:])[::-1]
t, x = 1, 0
for i in n:
    x += int(i) * t
    t *= 3
print(x)