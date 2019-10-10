class Stack:
    def __init__(self):
        self.items = []

    def is_empy(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    stack = Stack()
    for i in range(0, 5):
        stack.push(i)

    rev = []
    while stack.size():
        i = stack.pop()
        rev.append(i)
    print(rev)
