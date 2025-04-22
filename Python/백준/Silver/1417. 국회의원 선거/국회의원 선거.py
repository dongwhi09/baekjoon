l, x = [], 0
for i in range(int(input())):
    n = int(input())
    l.append(n)
while max(l) != l[0]:
    l[l.index(max(l))] -= 1
    l[0] += 1
    x += 1
c = l[0]
del l[0]
if c in l:
    print(x + 1)
else:
    print(x)