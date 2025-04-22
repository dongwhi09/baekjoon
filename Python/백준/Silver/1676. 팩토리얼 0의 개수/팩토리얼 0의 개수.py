n = int(input())
a = 1
x = 0
for i in range(1, n + 1):
    a *= i
a = str(a)
a_list = list(a)
a_list.reverse()
for j in a_list:
    if j != "0":
        print(x)
        break
    x += 1