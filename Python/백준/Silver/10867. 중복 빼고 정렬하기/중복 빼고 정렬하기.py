n = int(input())
num = set(map(int, input().split()))
num = list(num)
num.sort()
for i in range(len(num)):
    print(num[i], end=" ")