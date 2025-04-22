a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
elif a > b and a > c:
        print(a * 100)
elif b > a and b > c:
        print(b * 100)
elif c > a and c > b:
        print(c * 100)