n = int(input())
star = 2 * n - 1
blank = 0
for i in range(n):
    print(" " * blank + "*" * star)
    star -= 2
    blank += 1
star += 2
blank -= 1
for j in range(n - 1, 0, -1):
    star += 2
    blank -= 1
    print(" " * blank + "*" * star)