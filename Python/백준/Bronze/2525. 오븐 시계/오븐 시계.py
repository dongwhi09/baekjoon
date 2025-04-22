a, b = map(int, input().split())
c = int(input())
d = 0
e = 0
if c >= 60:
    d = c // 60
    e = c % 60
    a = a + d
    b = b + e
else:
    b = b + c
if b >= 60:
    a = a + b // 60
    b = b % 60
if a >= 24:
    a = a % 24
print(a, b)