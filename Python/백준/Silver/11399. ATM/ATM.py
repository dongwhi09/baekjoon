n = int(input())
l = list(map(int, input().split()))
s = [0] * n
for i in range(1, n):
    insert_point = i
    insert_value = l[i]
    for j in range(i - 1, -1, -1):
        if l[j] < l[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        l[j] = l[j - 1]
    l[insert_point] = insert_value
s[0] = l[0]
for i in range(1, n):
    s[i] = s[i - 1] + l[i]
result = 0
for i in s:
    result += i
print(result)