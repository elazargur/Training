# Enqueue: add a new element to the end of the queue.
# Dequeue: remove the element from the front of the queue and return it.
#
# 1 x   : Enqueue element  into the end of the queue.
# 2     : Dequeue the element at the front of the queue.
# 3     : Print the element at the front of the queue.


class MyQueue(object):
    def __init__(self):
        self.l = []

    def peek(self):
        return self.l[len(self.l) - 1]

    def pop(self):
        self.l.pop()

    def put(self, value):
        self.l.insert(0, value)


queue = MyQueue()
queue2 = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

