import sys
n, m = map(int, sys.stdin.readline().split())
d = {}
for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    d[a] = b
for _ in range(m):
    a = input()
    print(d[a])