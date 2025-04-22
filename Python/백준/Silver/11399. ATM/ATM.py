n = int(input())
l = list(map(int, input().split()))
l.sort(reverse = True)
x = 0
for i in range(n):
    x += sum(l)
    l[i] = 0
print(x)