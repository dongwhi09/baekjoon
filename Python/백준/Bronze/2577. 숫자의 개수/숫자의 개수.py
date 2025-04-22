num1 = int(input())
num2 = int(input())
num3 = int(input())
sum = list(str(num1 * num2 * num3))
answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in sum:
    answer[int(i)] += 1
for j in answer:
    print(j)