score = []
for i in range(8):
    score.append(int(input()))
o = []
answer = 0
for i in range(5):
    answer += max(score)
    o.append(score.index(max(score)) + 1)
    score[score.index(max(score))] = -1
o.sort()
print(answer)
for i in o:
    print(i, end=" ")