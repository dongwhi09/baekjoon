import sys
def my_round(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
n = my_round(n * 0.15)
l.sort()
try:
    if n > 0:
        print(my_round(sum(l[n:-n]) / len(l[n:-n])))
    else:
        print(my_round(sum(l) / len(l)))
except ZeroDivisionError:
    print(0)