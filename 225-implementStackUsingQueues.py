class MyStack(object):
    def __init__(self):
        self.c = []

    def pop(self):
        return self.c.pop()

    def push(self, x):
        self.c.append(x)

    def top(self):
        return self.c[-1]

    def empty(self):
        return len(self.c) == 0