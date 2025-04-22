ban = ["C", "A", "M", "B", "R", "I", "D", "G", "E"]
word = input()
for i in word:
    if i in ban:
        continue
    else:
        print(i, end="")