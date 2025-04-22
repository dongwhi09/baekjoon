import sys
input = sys.stdin.readline
list = []
for i in range(int(input())):
    n, d, m, y = input().rstrip().split()
    d, m, y = map(int, (d, m, y))
    list.append((y, m, d, n))
list.sort()
print(list[-1][3])
print(list[0][3])