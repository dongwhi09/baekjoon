n = int(input())
l = list(map(int, input().split()))
t, p = map(int, input().split())
x = 0
for i in l:
    if i == 0:
        continue
    elif i <= t:
        x += 1
    elif i % t == 0:
        x += i // t
    else:
        x += i // t + 1
y = n // p
z = n % p
print(x)
print(f'{y} {z}')