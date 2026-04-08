check_list, my_list, check = [0] * 4, [0] * 4, 0
def add(c):
    global check_list, my_list, check
    if c == 'A':
        my_list[0] += 1
        if my_list[0] == check_list[0]:
            check += 1
    elif c == 'C':
        my_list[1] += 1
        if my_list[1] == check_list[1]:
            check += 1
    elif c == 'G':
        my_list[2] += 1
        if my_list[2] == check_list[2]:
            check += 1
    elif c == 'T':
        my_list[3] += 1
        if my_list[3] == check_list[3]:
            check += 1
def remove(c):
    global check_list, my_list, check
    if c == 'A':
        if my_list[0] == check_list[0]:
            check -= 1
        my_list[0] -= 1
    elif c == 'C':
        if my_list[1] == check_list[1]:
            check -= 1
        my_list[1] -= 1
    elif c == 'G':
        if my_list[2] == check_list[2]:
            check -= 1
        my_list[2] -= 1
    elif c == 'T':
        if my_list[3] == check_list[3]:
            check -= 1
        my_list[3] -= 1
s, p = map(int, input().split())
string = input()
check_list = list(map(int, input().split()))
result, check = 0, 0
for i in check_list:
    if i == 0:
        check += 1
for i in range(p):
    add(string[i])
if check == 4:
    result += 1
for i in range(p, s):
    add(string[i])
    remove(string[i - p])
    if check == 4:
        result += 1
print(result)