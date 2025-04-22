word = input()
x = 0
for i in range(len(word)):
    if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
        x += 1
print(x)