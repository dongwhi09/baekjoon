for i in range(int(input())):
    h, m, s = map(int, input().split(':'))
    h, m, s = bin(h)[2:], bin(m)[2:], bin(s)[2:]
    for j in range(6 - len(h)):
        h = "0" + h
    for j in range(6 - len(m)):
        m = "0" + m
    for j in range(6 - len(s)):
        s = "0" + s
    for j in range(6):
        print(h[j], end="")
        print(m[j], end="")
        print(s[j], end="")
    print(" ", end="")
    print(h, end="")
    print(m, end="")
    print(s)