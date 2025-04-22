c, s = 100, 100
n = int(input())
for i in range(n):
    cd, sd = map(int, input().split())
    if cd > sd:
        s -= cd
    elif cd < sd:
        c -= sd
print(c)
print(s)