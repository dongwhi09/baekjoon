n = int(input())
total = 0
num = list(map(int, input().split()))
for i in num:
    total ^= i
print('koosaga' if total else 'cubelover')