import sys
input = sys.stdin.readline
x = 0
n, s = input().split()
for i in range(int(n)):
    name, count = input().split()
    name = name.split('_')
    if s in name:
        x += int(count)
print(x)