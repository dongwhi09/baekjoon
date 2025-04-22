a, b, v = map(int, input().split())
day = (v - a) / (a - b) + 1
print(int(day) if day == int(day) else int(day) + 1)