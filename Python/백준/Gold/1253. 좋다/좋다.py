n = int(input())
l = list(map(int, input().split()))
l.sort()
count = 0
for i in range(n):
    left, right = 0, n - 1
    while left < right:
        if l[left] + l[right] == l[i]:
            if left != i and right != i:
                count += 1
                break
            elif left == i:
                left += 1
            elif right == i:
                right -= 1
        elif l[left] + l[right] < l[i]:
            left += 1
        else:
            right -= 1
print(count)