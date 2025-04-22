n = int(input())
for i in range(n):
    result = input()
    score = 0
    sumScore = 0
    for j in result:
        if j == "O":
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)