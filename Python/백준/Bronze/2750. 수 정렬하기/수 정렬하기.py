n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
for i in range(n - 1):
    for j in range(n - 1 - i):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
for i in range(n):
    print(l[i])