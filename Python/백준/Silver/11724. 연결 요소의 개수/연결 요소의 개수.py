import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
l = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
def dfs(v):
    visited[v] = True
    for i in l[v]:
        if not visited[i]:
            dfs(i)
for _ in range(m):
    u, v = map(int, input().split())
    l[u].append(v)
    l[v].append(u)
result = 0
for i in range(1, n + 1):
    if not visited[i]:
        result += 1
        dfs(i)
print(result)