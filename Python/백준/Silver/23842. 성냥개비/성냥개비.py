match = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
x = int(input())
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        if x == match[i] + match[j] + match[k] + match[l] + match[m] + match[n] + 4:
                            if i * 10 + j + k * 10 + l == m * 10 + n:
                                print(str(i) + str(j) + "+" + str(k) + str(l) + "=" + str(m) + str(n))
                                exit()
print('impossible')