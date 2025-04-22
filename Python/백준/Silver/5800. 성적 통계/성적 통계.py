for i in range(1, int(input()) + 1):
    score = list(map(int, input().split()))
    student = score[0]
    score = score[1:]
    score.sort()
    x = 0
    for j in range(student - 1):
        if score[j + 1] - score[j] > x:
            x = score[j + 1] - score[j]
    print(f"Class {i}")
    print(f"Max {max(score)}, Min {min(score)}, Largest gap {x}")