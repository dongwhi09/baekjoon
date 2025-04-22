answer = []
sum, min = 0, 0
count = 0
for i in range(7):
    answer.append(int(input()))
answer.sort()
for i in range(6, -1, -1):
    if answer[i] % 2 != 0:
        sum += answer[i]
        min = answer[i]
        count += 1
if count == 0:
    print(-1)
else:
    print(sum)
    print(min)