n1 = int(input())
n2 = 0
for i in range(n1, 0, -1):
    print(" " * n2 + "*" * i)
    n2 += 1