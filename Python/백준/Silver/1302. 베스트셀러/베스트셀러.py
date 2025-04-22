import sys
input = sys.stdin.readline
sell = {}
for i in range(int(input())):
    name = input()
    if name in sell:
        sell[name] += 1
    else:
        sell[name] = 1
max_value = max(sell.values())
best = []
for key, value in sell.items():
    if value == max_value:
        best.append(key)
best = sorted(best)
print(best[0])