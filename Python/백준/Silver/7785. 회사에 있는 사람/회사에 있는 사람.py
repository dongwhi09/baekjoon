record, name = {}, []
for i in range(int(input())):
    person, action = input().split()
    record[person] = action
for key, val in record.items():
    if val == 'enter':
        name.append(key)
name.sort(reverse = True)
for i in name:
    print(i)