while True:
    a = input()
    if a == "0":
        break
    cnt = 2
    for i in a:
        if i == "1":
            cnt += 2
        elif i == "0":
            cnt += 4
        else:
            cnt += 3
    cnt += len(a) - 1
    print(cnt)