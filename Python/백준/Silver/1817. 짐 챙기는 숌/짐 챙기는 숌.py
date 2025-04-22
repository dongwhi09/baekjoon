n, m = map(int, input().split())
if n == 0:
    print(0)
else:
    book = list(map(int, input().split()))
    box, box_size = 0, 0
    for i in range(len(book)):
        if book[i] > box_size:
            box += 1
            box_size = m
            box_size -= book[i]
        else:
            box_size -= book[i]
    print(box)