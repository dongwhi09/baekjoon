n = int(input())
for i in range(n):
    name = input()
    g, b = 0, 0
    g += name.count('G')
    g += name.count('g')
    b += name.count('B')
    b += name.count('b')
    if g > b:
        print(f"{name} is GOOD")
    elif b > g:
        print(f"{name} is A BADDY")
    else:
        print(f"{name} is NEUTRAL")