word = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    if i in word:
        print(word.index(i), end=' ')
    else:
        print(-1, end=' ')