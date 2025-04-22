apart = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
for i in range(14):
    l = []
    for j in range(14):
        x = 0
        for k in range(j + 1):
            x += apart[i][k]
        l.append(x)
    apart.append(l)
for i in range(int(input())):
    k = int(input())
    n = int(input())
    print(apart[k][n - 1])