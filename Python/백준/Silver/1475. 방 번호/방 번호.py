n = input()
x = [0] * 10
for i in range(len(n)):
    x[int(n[i])] += 1
if (x[6] + x[9]) % 2 == 0:
    x[6] = (x[6] + x[9]) // 2
else:
    x[6] = (x[6] + x[9]) // 2 + 1
x[9] = 0
print(max(x))