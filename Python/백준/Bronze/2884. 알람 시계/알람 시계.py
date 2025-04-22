a, b = map(int, input().split())
if a == 0 and b < 45:
    a = 23
elif a != 0 and b < 45:
    a = a - 1
if b < 45:
    b = b - 45
    b = 60 + b
elif b >= 45:
    b = b - 45
print(a, b)