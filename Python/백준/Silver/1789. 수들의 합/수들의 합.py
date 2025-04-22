s = int(input())
total = 0
x = 0
while True:
    x += 1
    total += x
    if total > s:
        break
print(x - 1)