import sys
input = sys.stdin.readline
for i in range(int(input())):
    war = list(map(int, input().rstrip().split()))
    total_soldier = war[0]
    soldier_dic = {}
    for soldier_num in war[1:]:
        if soldier_num not in soldier_dic:
            soldier_dic[soldier_num] = 1
        else:
            soldier_dic[soldier_num] += 1
    if max(soldier_dic.values()) <= total_soldier//2:
        print('SYJKGW')
    else:
        print(max(soldier_dic, key=soldier_dic.get))