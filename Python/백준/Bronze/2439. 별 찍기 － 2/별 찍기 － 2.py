a = int(input())
b = a
for i in range(1, a + 1):
    b = b - 1
    print(" " * b + "*" * i)