import sys
n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
print(round(sum(l) / n))
l.sort()
print(l[n // 2])
d = {}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
m = max(d.values())
md = []
for i in d:
    if m == d[i]:
        md.append(i)
if len(md) == 1:
    print(md[0])
else:
    print(md[1])
print(max(l) - min(l))