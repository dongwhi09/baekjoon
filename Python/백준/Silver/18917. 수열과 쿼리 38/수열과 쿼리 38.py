import sys
input = sys.stdin.readline
sum, xor = 0, 0
for i in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        sum += q[1]
        xor ^= q[1]
    elif q[0] == 2:
        sum -= q[1]
        xor ^= q[1]
    elif q[0] == 3:
        print(sum)
    else:
        print(xor)