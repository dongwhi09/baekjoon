a = int(input())
b = int(input())
c, d, e = 0, 0, 0
for i in range(1, b + 1):
    c, d = map(int, input().split())
    e = c * d
    a = a - e
if a == 0:
    print("Yes")
else:
    print("No")