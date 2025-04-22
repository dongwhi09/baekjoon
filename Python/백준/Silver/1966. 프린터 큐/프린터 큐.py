for _ in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    x = 1
    while l:
        if l[0] < max(l):
            l.append(l.pop(0))
        else:
            if m == 0:
                break
            l.pop(0)
            x += 1
        if m > 0:
            m = m - 1
        else:
            m = len(l) - 1
    print(x)