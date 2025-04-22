n = int(input())
x = 0
result = 666
while True:
    if '666' in str(result):
        x += 1
    if x == n:
        break
    result += 1
print(result)