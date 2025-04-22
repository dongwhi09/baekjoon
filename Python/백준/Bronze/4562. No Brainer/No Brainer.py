a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    if b < c:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")