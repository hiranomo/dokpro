class Queue:
    def __init__(self):
        self.items = []

    def is_empy(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    queue = Queue()
    for i in range(5):
        queue.enqueue(i)
    print(queue.dequeue())
    print(queue.size())
