m = ["Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna stop"]
for i in range(int(input())):
    s = input()
    if s not in m:
        print("Yes")
        exit()
print("No")