n = int(input())
f = int(input())
a = n - (n % 100)
result = 0
while True:
    if a % f == 0:
        if result < 10:
            print(f"0{result}")
            break
        else:
            print(result)
            break
    else:
        result += 1
        a += 1