t = int(input())
answer = [0, 0, 0]
x = 1
if t % 10 != 0:
    print(-1)
    x = 0
if t // 300 > 0:
    answer[0] += t // 300
    t = t % 300
if t // 60 > 0:
    answer[1] += t // 60
    t = t % 60
if t // 10 > 0:
    answer[2] += t // 10
    t = t % 10
if x != 0:
    for i in range(3):
        print(answer[i], end=" ")