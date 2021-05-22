class Queue:
    def __init__(self):
        self.items=[]
        
    def enque(self,data):
        return self.items.insert(0,data)
        
    def deque(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items==[]

q=Queue()
q.enque('a')
q.enque('b')
q.enque('c')
print(q.isEmpty())