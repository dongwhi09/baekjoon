v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(x):
    global count
    visited[x] = True
    count += 1
    for node in graph[x]:
        if visited[node]:
            continue
        dfs(node)
count = 0
visited = [False for _ in range(v + 1)]
dfs(1)
print(count - 1)