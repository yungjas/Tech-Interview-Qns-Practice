# Queue: First In First Out

class Queuee:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, data):
        self.items.append(data)
    
    def dequeue(self):
        # remove the 1st item of the queue
        return self.items.pop(0)