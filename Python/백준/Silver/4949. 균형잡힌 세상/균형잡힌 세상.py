class Stack:
    def __init__(self):
        self.top = []
    def push(self, item):
        self.top.append(item)
    def pop(self):
        if not self.empty():
            return self.top.pop(-1)
        else:
            exit()
    def empty(self) -> bool:
        return len(self.top) == 0
def f(statement):
    stack = Stack()
    for ch in statement:
        if ch == "(" or ch == "[":
            stack.push(ch)
        elif ch == ")" or ch == "]":
            if stack.empty():
                return False
            else :
                left = stack.pop()
                if (ch == ")" and left != "(") or (ch == "]" and left != "["):
                    return False
    return stack.empty()
while True:
    s = input()
    if s == ".":
        break
    if f(s):
        print("yes")
    else:
        print("no")