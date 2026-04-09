n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
stack = []
num = 1
answer = []
for i in range(n):
    if l[i] >= num:
        while l[i] >= num:
            stack.append(num)
            num += 1
            answer.append('+')
        stack.pop()
        answer.append('-')
    else:
        if stack.pop() > l[i]:
            print("NO")
            exit()
        else:
            answer.append('-')
for i in answer:
    print(i)