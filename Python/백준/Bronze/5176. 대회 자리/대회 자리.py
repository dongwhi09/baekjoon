for i in range(int(input())):
    p, m = map(int, input().split())
    l = []
    for j in range(p):
        l.append(int(input()))
        l = list(set(l))
    print(p - len(l))