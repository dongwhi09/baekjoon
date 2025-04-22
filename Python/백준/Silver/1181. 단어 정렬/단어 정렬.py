import sys
n = int(sys.stdin.readline())
word = []
for i in range(n):
    word.append(sys.stdin.readline().strip())
set_word = set(word)
word = list(set_word)
word.sort()
word.sort(key = len)
for i in word:
    print(i)