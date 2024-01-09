class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return not bool(self.items)
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string
input_string = "Hello World"
print(reverse_string(input_string))