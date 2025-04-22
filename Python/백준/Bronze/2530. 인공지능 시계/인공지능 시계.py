a, b, c = map(int, input().split())
d = int(input())
c = c + d
b = b + c // 60
c = c % 60
a = a + b // 60
b = b % 60
a = a % 24
print(a, b, c)