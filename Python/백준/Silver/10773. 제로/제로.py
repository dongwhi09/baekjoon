s = []
for i in range(int(input())):
    n = int(input())
    if n == 0:
        del s[-1]
    else:
        s.append(n)
print(sum(s))