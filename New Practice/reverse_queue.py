class Queue:
    """
    implements a queue data structure
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return N

    def is_empty(self):
        return self.items[-1] if not self.is_empty() else None
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
def reverse_queue(queue):
    """
    reverse a queue useing a recursion
    """
    if queue.is_empty():
        return
    
    item = queue.dequeue()
    reverse_queue(queue)
    queue.enqueue(item)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)


reverse_queue(queue)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
