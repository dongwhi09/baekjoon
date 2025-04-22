n, cnt = input(), 0
l = list(input().split())
for i in range(len(l)):
    if l[i][-1] == n:
        cnt += 1
print(cnt)