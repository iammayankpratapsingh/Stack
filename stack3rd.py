class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return len(self.stack) == 0
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
def check_balance(expression):
    stack = Stack()
    for char in expression:
        if char in ["(", "{", "["]:
            stack.push(char)
        elif char in [")", "}", "]"]:
            if stack.isEmpty():
                return False
            else:
                popped_char = stack.pop()
                if popped_char == "(" and char != ")":
                    return False
                elif popped_char == "{" and char != "}":
                    return False
                elif popped_char == "[" and char != "]":
                    return False
    if stack.isEmpty():
        return True
    else:
        return False
expression = "{[()]} {[()()]}}"
print(check_balance(expression))