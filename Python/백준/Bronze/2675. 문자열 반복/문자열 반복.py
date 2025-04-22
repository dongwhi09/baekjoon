a = int(input())
for i in range(a):
    b, c = input().split()
    for j in range(len(c)):
        print(c[j] * int(b), end = '')
    print('')