class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        """Agregar Nodos al final de la lista"""
        new = Node(data)
        if self.head is None:
            self.head, self.tail = new, new
            self.size += 1
            return
        probe = self.head
        while probe.next:
            probe = probe.next
        probe.next = new
        self.size += 1
        return

    def push(self, data):
        new = Node(data)
        if self.head is None:
            self.append(data)
            return
        probe = self.head
        self.head = new
        new.next = probe
        self.size += 1

    def size(self):
        return (str(self.size))

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        previous = self.tail
        while current:
            if currrent.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data
            previous = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f"Data {data} found!")

    def clear(self):
        self.tail = None
        self.head = None
        self.size

class TwoWayNode:
    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous

if __name__ == '__main__':
    words = SinglyLinkedList()
    words.append("egg")
    words.append("ham")
    words.append("spam")
    words.append("juice")
    current = words.head
    while current is not None:
        print(current.data)
        current = current.next
    # for word in words.iter():
    #     print(word)
    # words.search("spam")
    # words.search("juice")
    # words.clear()
    # for word in words.iter():
    #     print(word)

    ## circular linked list

    head = None
    for value in range(1, 10):
        head = Node(value, head)

    probe = head
    print(probe.data)
    while probe.next != None:
        print(probe.data)
        probe = probe.next
    
    probe = head
    step = 10
    while step > 0 and probe.next != None:
        print(probe.data, end = ' ')
        probe = probe.next
        step -= 1
    print(probe.data)
    probe.next = head
    probe = head
    # while probe.next != None:
    #     print(probe.data, end='')
    #     probe = probe.next

    # Doublle linkedlist
    head = TwoWayNode(1)
    tail = head
    for data in range(2, 6):
        tail.next = TwoWayNode(data, tail)
        tail = tail.next
    probe = tail
    while probe != None:
        print(probe.data)
        probe = probe.previous
