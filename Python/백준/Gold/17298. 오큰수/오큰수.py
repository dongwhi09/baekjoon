n = int(input())
l = list(map(int, input().split()))
stack, answer = [], [0] * n
for i in range(n):
    while stack and l[stack[-1]] < l[i]:
        answer[stack.pop()] = l[i]
    stack.append(i)
while stack:
    answer[stack.pop()] = -1
for i in range(n):
    print(answer[i], end=' ')