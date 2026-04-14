import sys
input = sys.stdin.readline
m = [list(map(int, input().split())) for _ in range(10)]
s = [0, 5, 5, 5, 5, 5]
result = float('inf')
def fill(x, y, size, value):
    for i in range(y, y + size):
        for j in range(x, x + size):
            m[i][j] = value
def check(x, y, size):
    if x + size > 10 or y + size > 10:
        return False
    for i in range(y, y + size):
        for j in range(x, x + size):
            if m[i][j] != 1:
                return False
    return True
def backtrack(pos, used):
    global result
    if pos == 100:
        result = min(result, used)
        return
    if used >= result:
        return
    x, y = divmod(pos, 10)
    if m[y][x] == 1:
        for size in range(5, 0, -1):
            if s[size] > 0 and check(x, y, size):
                s[size] -= 1
                fill(x, y, size, 0)
                backtrack(pos + 1, used + 1)
                fill(x, y, size, 1)
                s[size] += 1
    else:
        backtrack(pos + 1, used)
backtrack(0, 0)
print(result if result != float('inf') else -1)