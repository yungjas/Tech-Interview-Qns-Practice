# Stack: Last In First Out

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, data):
        return self.items.append(data)
    
    def pop(self):
        # removes the last item that has entered the stack
        return self.items.pop()