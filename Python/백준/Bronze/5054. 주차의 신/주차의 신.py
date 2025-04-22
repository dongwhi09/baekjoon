for i in range(int(input())):
    n = int(input())
    shop = list(map(int, input().split()))
    print((max(shop) - min(shop)) * 2)