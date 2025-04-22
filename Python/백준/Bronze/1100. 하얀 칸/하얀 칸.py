x = 0
for i in range(8):
    l = input()
    if i % 2 == 0:
        for j in range(0, 8, 2):
            if l[j] == "F":
                x += 1
    else:
        for j in range(1, 8, 2):
            if l[j] == "F":
                x += 1
print(x)