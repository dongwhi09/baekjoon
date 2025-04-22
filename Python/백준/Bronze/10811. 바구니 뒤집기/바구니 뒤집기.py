l, n = map(int, input().split())
answer = [i for i in range(1, l + 1)]
for i in range(n):
    a, b = map(int, input().split())
    temp = answer[a - 1:b]
    temp.reverse()
    answer[a - 1:b] = temp
for i in range(l):
    print(answer[i], end=' ')