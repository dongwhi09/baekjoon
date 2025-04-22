hint = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a = input()
b = input()
arr = []
for i in range(len(a)):
    arr.append(hint[ord(a[i]) - 65])
    arr.append(hint[ord(b[i]) - 65])
temp = []
while len(arr) != 2:
    for i in range(1, len(arr)):
        temp.append((arr[i] + arr[i - 1]) % 10)
    arr = temp
    temp = []
print(str(arr[0]) + str(arr[1]))