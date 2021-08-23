from heapq import heappush, heappop

class Stack:

    def __init__(self):
        self.data = []

    @property
    def empty(self):
        return len(self.data) == 0

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()


class Queue:

    def __init__(self):
        self.data = []

    @property
    def empty(self):
        return len(self.data) == 0

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop(0)


class PriorityQueue:

    def __init__(self):
        self.data = []

    @property
    def empty(self):
        return len(self.data) == 0

    def push(self, element):
        heappush(self.data, element)

    def pop(self):
        return heappop(self.data)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    while not(s.empty):
        print(s.pop())
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    while not(q.empty):
        print(q.pop())
    p = PriorityQueue()
    p.push(2)
    p.push(3)
    p.push(1)
    while not(p.empty):
        print(p.pop())
