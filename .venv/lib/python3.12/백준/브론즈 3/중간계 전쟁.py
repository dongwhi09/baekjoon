t = int(input())
for z in range(1, t + 1):
    gl = list(map(int, input().split()))
    el = list(map(int, input().split()))
    good = gl[0] + gl[1] * 2 + (gl[2] + gl[3]) * 3 + gl[4] * 4 + gl[5] * 10
    evil = el[0] + (el[1] + el[2] + el[3]) * 2 + el[4] * 3 + el[5] * 5 + el[6] * 10
    if evil > good:
        print(f"Battle {z}: Evil eradicates all trace of Good")
    elif good > evil:
        print(f"Battle {z}: Good triumphs over Evil")
    else:
        print(f"Battle {z}: No victor on this battle field")