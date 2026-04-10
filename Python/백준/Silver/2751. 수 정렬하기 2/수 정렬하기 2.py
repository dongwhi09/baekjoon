import sys
l = []
for i in range(int(input())):
    l.append(int(sys.stdin.readline()))
l.sort()
for i in l:
    print(i)