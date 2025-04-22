n, q = map(int, input().split())
num = list(map(int, input().split()))
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        print(sum(num[query[1] - 1:query[2]]))
        temp = num[query[1] - 1]
        num[query[1] - 1] = num[query[2] - 1]
        num[query[2] - 1] = temp
    else:
        print(sum(num[query[1] - 1:query[2]]) - sum(num[query[3] - 1:query[4]]))