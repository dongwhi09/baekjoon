n = int(input())
num = []
for i in range(n):
    num.append(str(input()))
for i in range(1, len(num[0]) + 1):
    results = []
    for j in range(n):
        if num[j][-i:] in results:
            break
        else:
            results.append(num[j][-i:])
    if len(results) == n:
        print(i)
        break