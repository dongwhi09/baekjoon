a, b, c = map(int, input().split())
if (a * b) <= c:
    print(0)
elif (a * b) > c:
    print(a * b - c)