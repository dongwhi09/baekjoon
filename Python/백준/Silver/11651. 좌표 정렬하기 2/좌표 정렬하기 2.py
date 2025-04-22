answer = []
for i in range(int(input())):
	x, y = map(int,input().split())
	answer.append((x, y))
answer.sort(key = lambda y : (y[1], y[0]))
for i in answer:
	print(i[0], i[1])