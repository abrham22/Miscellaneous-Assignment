
class stack():
    def __init__(self): #constructor
        self.l = []
        
    def length(self): #length of items
        return len(self.l)
    
    def isEmpty(self): #check if empty to prevent underFlow
        return len(self.l)==0

    def push(self,item): #insert item to top of stack
        self.l.append(item)
        
    def pop(self): #delete item from stack
        return self.l.pop()

    def peek(self): #check position of stack
        return self.l[-1]
