a, b, c = map(int, input().split())
if (a > b and a < c) or (a < b and a > c):
    print(a)
elif (b > a and b < c) or (b < a and b > c):
    print(b)
elif (c > a and c < b) or (c < a and c > b):
    print(c)
elif (a == b and a > c) or (a == c and a > b):
    print(a)
elif (a == b and a > c) or (a == c and a < b):
    print(a)
elif (b == a and b > c) or (b == c and b > a):
    print(b)
elif (b == a and b > c) or (b == c and b < a):
    print(b)
elif (c == a and c > b) or (c == b and c > a):
    print(c)
elif (c == a and c > b) or (c == b and c < a):
    print(c)
else:
    print(a)