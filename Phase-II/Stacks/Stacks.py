class node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
class Stack:
    def __init__(self):
        self.top = None
    def push(self,data):
        temp = node(data)
        temp.next = self.top
        self.top = temp
        # self.top = node(data,self.data)
    def pop(self):
        if self.top == None:
            raise Exception('UnderFlow')
        temp = self.top.data
        self.top = self.top.next
        return temp
    def isEmpty(self):
        return self.top == None
    def printStack(self):
        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next
a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.pop()
print(a.isEmpty())
a.printStack()