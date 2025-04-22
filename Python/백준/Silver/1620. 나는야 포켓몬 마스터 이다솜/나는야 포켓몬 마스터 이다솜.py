import sys
n, m = map(int, sys.stdin.readline().split())
name = {}
for i in range(1, n + 1):
    x = sys.stdin.readline().strip()
    name[i] = x
    name[x] = i
for i in range(m):
    x = sys.stdin.readline().strip()
    if x.isdigit():
        x = int(x)
    print(name[x])