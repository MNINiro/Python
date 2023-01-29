class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def get_queue(self):
        return self.items

queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
print(queue.dequeue()) # Output: A
print(queue.peek()) # Output: B
