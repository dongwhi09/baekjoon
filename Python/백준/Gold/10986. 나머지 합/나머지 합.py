import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0] * n
c = [0] * m
prefix_sum[0] = numbers[0]
result = 0
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i]
for i in range(n):
    remainder = prefix_sum[i] % m
    if remainder == 0:
        result += 1
    c[remainder] += 1
for i in range(m):
    if c[i] > 1:
        result += (c[i] * (c[i] - 1) // 2)
print(result)