import sys
n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
s = [0]
sum = 0
for i in l:
    sum += i
    s.append(sum)
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(s[j] - s[i - 1])