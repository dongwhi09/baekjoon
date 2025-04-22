import sys
l = []
for i in range(int(input())):
    n = int(sys.stdin.readline())
    l.append(n)
l.sort()
for i in l:
    print(i)