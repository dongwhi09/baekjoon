import sys
input = sys.stdin.readline
arr = [0, 1, 2, 4]
for i in range(7):
    arr.append(arr[len(arr) - 1] + arr[len(arr) - 2] + arr[len(arr) - 3])
for i in range(int(input())):
    print(arr[int(input())])