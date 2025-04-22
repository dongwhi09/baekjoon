n = int(input())
blank = n - 1
for i in range(1, n + 1):
    print(" " * blank + "*" * i)
    blank -= 1
blank = 0
for j in range(n - 1, 0, -1):
    blank += 1
    print(" " * blank + "*" * j)