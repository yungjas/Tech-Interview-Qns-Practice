class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, data):
        return self.items.append(data)
    
    def pop(self):
        return self.items.pop()