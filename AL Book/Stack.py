class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def get_stack(self):
        return self.items

stack = Stack()
stack.push("A")
stack.push("B")
print(stack.pop()) # Output: B
print(stack.peek()) # Output: A
