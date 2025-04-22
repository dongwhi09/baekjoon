string = input()
if string[0] != '"' or string[-1] != '"' or len(string) < 3:
    print('CE')
else:
    print(string[1:-1])