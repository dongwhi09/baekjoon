n = int(input())
blank = n - 1
star = 1
for i in range(n):
    print(" " * blank + "*" * star)
    blank -= 1
    star += 2