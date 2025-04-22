import sys
d = {}
for i in range(int(input())):
    a, b = sys.stdin.readline().split('.')
    if b not in d:
        d[b] = 1
    else:
        d[b] += 1
d = sorted(d.items())
for k, v in d:
    print(k.rstrip(), v)