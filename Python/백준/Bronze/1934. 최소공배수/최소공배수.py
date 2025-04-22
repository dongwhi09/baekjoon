import sys

n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    aa, bb = a, b

    while bb != 0:
        aa = aa % bb
        aa, bb = bb, aa

    print(a * b // aa)