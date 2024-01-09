class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return self.stack == []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
    def size(self):
        return len(self.stack)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop()) 
print(stack.peek()) 
print(stack.size()) 
