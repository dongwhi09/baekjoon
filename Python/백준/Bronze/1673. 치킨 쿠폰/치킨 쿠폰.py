try:
    while True:
        n, k = map(int, input().split())
        x = n
        while n >= k:
            x += n // k
            n = n // k + n % k
        print(x)
except EOFError:
    exit()