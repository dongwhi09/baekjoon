n = int(input())
card = []
for i in range(1, n + 1):
    card.append(i)
while True:
    if len(card) == 0:
        break
    print(card[0], end=" ")
    card.pop(0)
    if len(card) == 0:
        break
    temp = card[0]
    card.pop(0)
    card.append(temp)