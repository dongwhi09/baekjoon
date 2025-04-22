n, m = map(int, input().split())
arr, cnt = [], 64
for i in range(n):
    arr.append(input())
for x in range(n - 7):
    for y in range(m - 7):
        w = 0
        b = 0
        for i in range(x, x + 8):
            for j in range(y, y + 8):
                if (i + j) % 2 == 0:
                    if arr[i][j] != 'W':
                        w += 1
                    else:
                        b += 1
                else:
                    if arr[i][j]!='W':
                        b += 1
                    else:
                        w += 1
        if w < cnt:
            cnt = w
        if b < cnt:
            cnt = b
print(cnt)