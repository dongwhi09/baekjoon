a = int(input())
b = list(map(int, input().split()))
min = b[0]
max = b[0]
for i in range(0, a):
    if b[i] < min:
        min = b[i]
    if b[i] > max:
        max = b[i]
print(min, max)