n, k = map(int, input().split())

answer = []

for i in range(n):
    answer.append(list(map(int, input().split())))

for i in range(n):
    for l in range(k):
        for j in range(n):
            for m in range(k):
                print(answer[i][j], end = ' ')
        print()