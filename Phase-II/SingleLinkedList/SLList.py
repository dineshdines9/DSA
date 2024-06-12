class node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class llist:
    def __init__(self,head=None):
        self.head = head
    def size(self):
        count = 0
        temp = self.head
        while temp != None :
            count += 1
            temp = temp.next
        return count
    def insert_begin(self,data):
        self.head = node(data,self.head)
    def insert_end(self,data):
        if self.head == None:
            self.head = node(data)
            return
        temp = self.head
        while temp.next != None :
            temp = temp.next
        temp.next = node(data)
    def insert_position(self,data,pos):
        if self.head == None:
            self.head = node(data)
            return
        elif pos == 1:
            self.insert_begin(data)
        elif pos >= self.size():
            self.insert_end(data)
        else:
            temp = self.head
            k = 1
            while temp.next != None  and k < pos:
                temp = temp.next
                k += 1
            temp.next = node(data,temp.next)
    def delete_begin(self):
        temp = self.head
        self.head = self.head.next
        del temp
    def delete_end(self):
        prev = None
        current = self.head
        while current.next != None:
            prev = current
            current = current.next
        prev.next = None
        del current
    def delete_data(self,data):
        current = self.head
        prev = None
        while current != None and current.data != data:
            prev = current
            current = current.next
        if current == None:
            raise Exception('No Data Found')
        prev.next = current.next
    def printllist(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
a = llist()
a.insert_end(1)
a.insert_end(2)
a.insert_end(3)
a.insert_end(4)
a.insert_end(5)
a.insert_end(7)
a.insert_position(0,1)
a.insert_position(9,7)
a.insert_position(5.5,5)
a.delete_begin()
a.delete_data(5.5)
a.delete_data(39)
a.printllist()