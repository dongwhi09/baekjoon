k = int(input())
for i in range(1, k + 1):
    head = int(input())
    action = input()
    for j in range(len(action)):
        if action[j] == "c":
            head += 1
        else:
            head -= 1
    print(f"Data Set {i}:")
    print(head)
    print()