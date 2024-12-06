record = {"enter":[]}
for i in range(int(input())):
    person, action = input().split()
    if action == "enter":
        record["enter"].append(person)
    else:
        record["enter"].remove(person)
for i in record["enter"]:
    print(i)