while True:
    try:
        arr = list(map(int, input().split()))
        size = arr[0]
        arr = arr[1:]
        check = []
        for i in range(1, len(arr)):
            check.append(i)
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) in check:
                check.remove(abs(arr[i] - arr[i + 1]))
            else:
                print("Not jolly")
                break
        if not check:
            print("Jolly")
    except:
        break