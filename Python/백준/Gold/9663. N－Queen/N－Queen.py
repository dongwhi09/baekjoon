import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
result = 0
cols = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)
def backtrack(row):
    global result
    if row == n:
        result += 1
        return
    for col in range(n):
        if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
            backtrack(row + 1)
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False
backtrack(0)
print(result)