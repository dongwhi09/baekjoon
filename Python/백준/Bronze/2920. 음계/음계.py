answer = list(input().split())
a = 1
b = 8
for i in range(8):
    if answer[i] == str(a):
        a += 1
    if answer[i] == str(b):
        b -= 1
    else:
        continue
if a == 9:
    print("ascending")
elif b == 0:
    print("descending")
else:
    print("mixed")