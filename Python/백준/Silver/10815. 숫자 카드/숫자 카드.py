import sys
n = int(sys.stdin.readline())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
for i in m_list:
    low, high = 0, n - 1
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if n_list[mid] > i:
            high = mid - 1
        elif n_list[mid] < i:
            low = mid + 1
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')