x = int(input())
x = bin(x)
x = x[2:]
count = 0
for i in range(len(x)):
    if x[i] == "1":
        count += 1
print(count)