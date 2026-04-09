import sys
input = sys.stdin.readline
n = int(input())
l, result = [], 0
for i in range(n):
    l.append((int(input()), i))
sorted_l = sorted(l)
for i in range(n):
    if result < sorted_l[i][1] - i:
        result = sorted_l[i][1] - i
print(result + 1)