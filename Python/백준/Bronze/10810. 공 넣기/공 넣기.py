l, n = map(int, input().split())
answer = [0] * (l + 1)
for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(a, b + 1):
        answer[j] = c
for i in range(1, l + 1):
    print(answer[i], end=' ')