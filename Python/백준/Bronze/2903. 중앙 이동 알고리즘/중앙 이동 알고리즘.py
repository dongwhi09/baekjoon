n = int(input())
dot = 2
x = 1
for i in range(n):
    dot += x
    x *= 2
print(dot * dot)