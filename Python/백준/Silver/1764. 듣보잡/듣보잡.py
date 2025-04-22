import sys
input = sys.stdin.readline
n, m = map(int, input().split())
name1 = set()
name2 = set()
for i in range(n):
    name1.add(input())
for i in range(m):
    name2.add(input())
name = list(name1 & name2)
name.sort()
print(len(name))
for i in name:
    print(i, end="")