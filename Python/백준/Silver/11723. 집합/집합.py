# 집합
import sys
m = int(sys.stdin.readline())
s = set()
for i in range(m):
    action = sys.stdin.readline().strip().split()
    if len(action) == 1:
        if action[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        action[1] = int(action[1])
        if action[0] == "add":
            s.add(action[1])
        elif action[0] == "remove":
            s.discard(action[1])
        elif action[0] == "check":
            print(1 if action[1] in s else 0)
        elif action[0] == "toggle":
            if action[1] in s:
                s.discard(action[1])
            else:
                s.add(action[1])