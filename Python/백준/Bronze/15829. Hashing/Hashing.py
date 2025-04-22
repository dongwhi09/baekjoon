l = int(input())
word = input()
x = 0
for i in range(l):
    num = ord(word[i]) - 96
    x += num * (31 ** i)
print(x % 1234567891)