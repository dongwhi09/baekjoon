t = int(input())
for z in range(1, t + 1):
    a, b, c, d, e, f = map(int, input().split())
    g, h, i, j, k, l, m = map(int, input().split())
    good = a * 1 + b * 2 + c * 3 + d * 3 + e * 4 + f * 10
    evil = g * 1 + h * 2 + i * 2 + j * 2 + k * 3 + l * 5 + m * 10
    if evil > good:
        print(f"Battle {z}: Evil eradicates all trace of Good")
    elif good > evil:
        print(f"Battle {z}: Good triumphs over Evil")
    else:
        print(f"Battle {z}: No victor on this battle field")