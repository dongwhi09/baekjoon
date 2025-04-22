n = int(input())
stack, op = [], []
count = 1
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop(-1)
        op.append('-')
    else:
        print("NO")
        exit()
for i in op:
    print(i)