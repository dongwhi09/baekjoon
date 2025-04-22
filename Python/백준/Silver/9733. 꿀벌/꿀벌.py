import sys
work = {'Re': 0, 'Pt': 0, 'Cc': 0, 'Ea': 0, 'Tb': 0, 'Cm': 0, 'Ex': 0}
try:
    a = sys.stdin.read().split()
except:
    a = []
l = len(a)
for i in a:
    if i in work:
        work[i] += 1

for k, v in work.items():
    if v:
        print(f"{k} {v} {v / l:.2f}")
    else:
        print(f"{k} 0 0.00")
print(f"Total {l} 1.00")