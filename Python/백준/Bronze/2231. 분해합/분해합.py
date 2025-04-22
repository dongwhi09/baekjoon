n = int(input())
cnt = 0
while True:
    cnt += 1
    length = len(str(cnt))
    x = cnt
    for i in range(length):
        x += int(str(cnt)[i])
    if x == n:
        print(cnt)
        break
    if cnt == 1000000:
        print(0)
        break