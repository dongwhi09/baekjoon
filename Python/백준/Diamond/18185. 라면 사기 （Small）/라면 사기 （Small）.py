import sys
def buy1(n):  # 1개 살 경우
    global result
    result += 3 * x[n]

def buy2(n):  # 2개 살 경우
    global result
    least = min(x[n:n + 2])
    x[n] -= least
    x[n + 1] -= least
    result += 5 * least

def buy3(n):  # 3개 살 경우
    global result
    least = min(x[n:n + 3])
    x[n] -= least
    x[n + 1] -= least
    x[n + 2] -= least
    result += 7 * least

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split())) + [0, 0]
result = 0
for i in range(len(x) - 2):
    if x[i + 1] > x[i + 2]:
        m = min(x[i], x[i + 1] - x[i + 2])
        x[i] -= m
        x[i + 1] -= m
        result += 5 * m
        buy3(i)
        buy1(i)
    else:
        buy3(i)
        buy2(i)
        buy1(i)
print(result)