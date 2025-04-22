import sys
k, n = map(int, sys.stdin.readline().split())
l = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(l)
while start <= end:
    mid = (start + end) // 2
    line = 0
    for i in l:
        line += i // mid
    if line >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)