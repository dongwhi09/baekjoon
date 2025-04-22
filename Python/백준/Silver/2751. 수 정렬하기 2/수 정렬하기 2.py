import sys
n = int(input())
answer = []
for i in range(n):
    answer.append(int(sys.stdin.readline()))
answer.sort()
for i in answer:
    print(i)