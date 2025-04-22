n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])
arr.sort(key=lambda k:k[1])
arr.sort(key=lambda k:k[0])
for i in range(n):
    print(arr[i][0], arr[i][1])