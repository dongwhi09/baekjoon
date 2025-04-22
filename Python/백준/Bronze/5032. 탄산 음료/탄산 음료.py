e, f, c = map(int, input().split())
e += f
x = 0
while e >= c:
    x += e // c
    e = e // c + e % c
print(x)