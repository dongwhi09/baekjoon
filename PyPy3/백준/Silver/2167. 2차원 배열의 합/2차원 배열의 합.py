import sys
input = sys.stdin.readline
l = []
n, m = map(int, input().split())
for i in range(n):
    l.append(list(map(int, input().split())))
for k in range(int(input())):
    sum = 0
    i, j, x, y = map(int, input().split())
    for a in range(i - 1, x):
        for b in range(j - 1, y):
            sum += l[a][b]
    print(sum)