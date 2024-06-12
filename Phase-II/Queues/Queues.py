class node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
class queue:
    def __init__(self):
        self.rear = None
        self.front = None
    def insert(self,data):
        # Under Flow Eror
        # As it is the implementation of LL , Overflow do not occur
        if self.rear == self.front == None:
            self.rear = self.front = node(data)
        else:
            self.rear.next = node(data)
            self.rear = self.rear.next
    def delete(self):
        temp = self.front.data
        self.front = self.front.next
        return temp
    def printQueue(self):
        temp = self.front
        while temp != self.rear:
            print(temp.data)
            temp = temp.next
        print(temp.data)
a = queue()
a.insert(1)
a.insert(2)
a.insert(3)
a.delete()
a.printQueue()
        