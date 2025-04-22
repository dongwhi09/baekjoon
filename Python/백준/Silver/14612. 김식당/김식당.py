import sys
N, m = map(int, sys.stdin.readline().split())
order = []
for _ in range(N):
    line = sys.stdin.readline().rstrip().split()
    if len(line) == 3:
        n, t = map(int, line[1:])
        order.append([n, t])
    elif len(line) == 2:
        n = int(line[1])
        for i in range(len(order)):
            if order[i][0] == n:
                order.pop(i)
                break
    elif len(line) == 1:
        order.sort(key=lambda x: (x[1], x[0]))
    if len(order) == 0:
        print('sleep')
    else:
        tables = []
        for table, time in order:
            tables.append(table)
        print(*tables)