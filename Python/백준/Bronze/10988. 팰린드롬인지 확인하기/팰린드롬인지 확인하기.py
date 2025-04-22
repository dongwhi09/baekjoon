word = input()
if word[::1] == word[::-1]:
    print(1)
else:
    print(0)