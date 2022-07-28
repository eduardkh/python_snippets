class Stack():
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def __str__(self):
        return ','.join(map(str, self.stack))


stack = Stack()
print(f"is the stack empty: {stack.isEmpty()}")
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(f"popping: {stack.pop()}")
print(f"is the stack empty: {stack.isEmpty()}")
print(f"total in stack: {stack}")
