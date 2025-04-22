answer = []
for i in range(10):
    n = int(input())
    if n % 42 not in answer:
        answer.append(n % 42)
print(len(answer))