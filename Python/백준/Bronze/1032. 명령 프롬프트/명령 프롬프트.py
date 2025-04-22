l, ans, x = [], [], ""
for i in range(int(input())):
    l.append(input())
for i in range(len(l[0])):
    cnt = 0
    x = l[0][i]
    for j in range(1, len(l)):
        if l[j][i] == x:
            cnt += 1
    if cnt == len(l) - 1:
        ans.append(x)
    else:
        ans.append("?")
for i in ans:
    print(i, end='')