for _ in range(int(input())):
    g = int(input())
    l = [int(input()) for i in range(g)]
    result = 0
    while True:
        result += 1
        if len({i % result for i in l}) == g:
            print(result)
            break