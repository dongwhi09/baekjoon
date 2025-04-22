answer = []
for i in range(101):
    answer.append([])
    for j in range(101):
        answer[i].append(0)
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            answer[x + j][y + k] = 1
count = 0
for i in range(101):
    for j in range(101):
        if answer[i][j] == 1:
            count += 1
print(count)