class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

    def traverse(self):
        total_items = self.size
        for item in range(total_items):
            print(self.items[item])

class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        self.inbound_stack.append(data)

    def dequeue(self):
        while self.inbound_stack:
            self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop(0) if self.outbound_stack else None



if __name__ == "__main__":
    # food = ListQueue()
    # food.enqueue('eggs')
    # food.enqueue('ham')
    # food.enqueue('spam')
    # print(food.dequeue())
    # print("DSAF")
    # food.traverse()

    numbers = Queue()
    numbers.enqueue(5)
    numbers.enqueue(6)
    numbers.enqueue(7)
    print(numbers.inbound_stack)
    print(numbers.dequeue())
    print(numbers.outbound_stack)
    numbers.enqueue(8)
    print(numbers.inbound_stack)
    print(numbers.dequeue())
    print(numbers.outbound_stack)
    print(numbers.dequeue())
    print(numbers.dequeue())
    print(numbers.dequeue())


