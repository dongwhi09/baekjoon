n, m = map(int, input().split())
s = [0] * m
visited = [False] * n
def backtrack(length):
    if length == m:
        print(' '.join(str(x + 1) for x in s))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            s[length] = i
            backtrack(length + 1)
            visited[i] = False
backtrack(0)