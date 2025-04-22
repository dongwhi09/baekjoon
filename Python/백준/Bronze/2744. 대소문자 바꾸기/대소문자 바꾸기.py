word = input()
for i in word:
    i = ord(i)
    if i >= 97:
        i -= 32
        i = chr(i)
    else:
        i += 32
        i = chr(i)
    print(i, end="")