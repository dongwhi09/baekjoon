n = int(input())
m = int(input())
l = list(map(int, input().split()))
l.sort()
left, right, count = 0, n - 1, 0
while left < right:
    if l[left] + l[right] < m:
        left += 1
    elif l[left] + l[right] > m:
        right -= 1
    else:
        count += 1
        left += 1
        right -= 1
print(count)