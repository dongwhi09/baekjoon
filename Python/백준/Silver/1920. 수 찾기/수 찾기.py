n = int(input())
n_l = set(map(int, input().split()))
m = int(input())
m_l = list(map(int, input().split()))
for i in m_l:
    if i in n_l:
        print(1)
    else:
        print(0)