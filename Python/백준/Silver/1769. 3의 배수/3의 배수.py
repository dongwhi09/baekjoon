n = list(input())
count = 0
while len(n) != 1:
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    n = list(str(sum))
    count += 1
print(count)
if int(n[0]) % 3 == 0:
    print("YES")
else:
    print("NO")