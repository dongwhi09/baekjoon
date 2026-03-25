import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = list(map(int, input().split()))
sum = 0
for i in range(len(l)):
    sum += l[i]
    l[i] = sum
for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        print(l[j - 1])
    else:
        print(l[j - 1] - l[i - 2])