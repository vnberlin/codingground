# Queue using 2 Stacks
class Stack:
    def __init__(self, size):
        self.size = size
        self.lst = []
        
    def push(self, data):
        if len(self.lst) < self.size:
            self.lst.append(data)
            return True
        else:
            return False
    
    def pop(self):
        return self.lst.pop()
        
    def get_size(self):
        return self.size
        
    def isEmpty(self):
        return self.lst == []
        
class Queue:
    def __init__(self,size):
        self.size = size
        self.instack = Stack(self.size)
        self.outstack = Stack(self.size)
        
    def enqueue(self, data):
        t = self.instack.push(data)
        if t:
            print "queued data : %d" % data
        else:
            print "error: queue full"
            
    def dequeue(self):
        if self.instack.isEmpty() and self.outstack.isEmpty():
            print "queue empty"
        elif self.outstack.isEmpty() and not(self.instack.isEmpty()):
            #print "t2-a"
            while(not self.instack.isEmpty()):
                self.outstack.push(self.instack.pop())
            
            return self.outstack.pop()
        else:
            #print "t2-b"
            return self.outstack.pop()
            
    def __private_order_queue(self):
        pass
    
def main():
    q = Queue(5)
    test1 = q.dequeue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    
    test2 = q.dequeue()
    t21 = q.dequeue()
    t22 = q.dequeue()
    t23 = q.dequeue()
    t24 = q.dequeue()
    print "dequeued : "
    print test2,t21,t22,t23,t24
    test3 = q.dequeue()

if __name__ == '__main__':
    main()
    