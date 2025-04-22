n = int(input())
m = int(input())
nl = list(map(int, input().split()))
nl.sort()
cnt, start, end = 0, 0, len(nl) - 1
while start < end:
    result = nl[start] + nl[end]
    if result > m:
        end -= 1
    elif result < m:
        start += 1
    else:
        cnt += 1
        start += 1
        end -= 1
print(cnt)