class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        data = None
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
        return data

    def peek(self):
        if self.top:
            return self.top.data
        return None

    def clear(self):
        while self.top:
            self.pop()

    def search(self, data):
        top = self.top
        while top != None:
            if top.data == data:
                return True
            top = top.next
        return False
if __name__ == '__main__':
    food = Stack()
    food.push('egg')
    food.push('ham')
    food.push('spam')

    # print(food.pop())
    # print(food.peek())
    # food.clear()
    # print(food.peek())
    print(food.search('afgasdf'))

    probe = food.top
    print(probe.data)
    print(probe.next)
    while probe != None:
        print(probe.data)
        probe = probe.next
