from random import shuffle
num_li = list(range(1, 10001))
shuffle(num_li)
while True:
    A = num_li.pop()
    print(f'? A {A}', flush = True)
    k = int(input())
    if k == 1:
        break
num_li = list(range(1, 10001))
shuffle(num_li)
while True:
    B = num_li.pop()
    print(f'? B {B}', flush = True)
    k = int(input())
    if k == 1:
        break
print(f'! {A+B}', flush = True)