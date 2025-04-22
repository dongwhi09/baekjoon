l, n = map(int, input().split())
answer = list(range(1, l + 1))
temp = 0
for i in range(n):
    a, b = map(int, input().split())
    temp = answer[a - 1]
    answer[a - 1] = answer[b - 1]
    answer[b - 1] = temp
for i in range(l):
    print(answer[i], end=' ')