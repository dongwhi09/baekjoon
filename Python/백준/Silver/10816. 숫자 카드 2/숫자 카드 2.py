import sys
input = sys.stdin.readline
n = int(input())
nl = list(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))
answer = {}
for i in nl:
    if i in answer:
        answer[i] += 1
    else:
        answer[i] = 1
for i in ml:
    result = answer.get(i)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")