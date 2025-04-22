n = int(input())
star = 2 * n - 1
blank = 0
for i in range(n):
    print(" " * blank + "*" * star)
    star -= 2
    blank += 1