n = int(input())
blank = 2 * n - 2
for i in range(1, n + 1):
    print("*" * i + " " * blank + "*" * i)
    blank -= 2
blank = 0
for j in range(n - 1, 0, -1):
    blank += 2
    print("*" * j + " " * blank + "*" * j)