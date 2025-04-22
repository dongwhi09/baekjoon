import sys
l = []
for i in range(int(sys.stdin.readline())):
    a = list(map(str, sys.stdin.readline().split()))
    if len(a) == 2:
        l.append(a[1])
    if a[0] == "pop":
        if l:
            print(l[-1])
            l.pop(-1)
        else:
            print(-1)
    if a[0] == "size":
        print(len(l))
    if a[0] == "empty":
        if l:
            print(0)
        else:
            print(1)
    if a[0] == "top":
        if l:
            print(l[-1])
        else:
            print(-1)