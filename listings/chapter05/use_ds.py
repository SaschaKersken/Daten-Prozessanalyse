from data_structures import Stack, Queue

s = Stack()
s.push(1)
s.push(2)
s.push(3)
while s.empty == False:
    print(s.pop())

q = Queue()
q.push(1)
q.push(2)
q.push(3)
while q.empty == False:
    print(q.pop())
