# class llist:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next
# def printllist(head):
#     while head != None:
#         print(head.data)
#         head = head.next
# def insertatend(head,data):
#     while head.next != None:
#         head = head.next
#     head.next = llist(data)
# head = llist(1)
# insertatend(head,2)
# insertatend(head,3)
# insertatend(head,4)
# printllist(head)
class node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class llist:
    def __init__(self,head=None):
        self.head = head
    def insert(self,data):
    #     self.head = node(data,self.head)
        if self.head == None:
            self.head = node(data)
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node(data)
    def printll(self):
        temp = self.head
        while temp.next != None:
            print(temp.data)
            temp = temp.next
        print(temp.data)
a = llist()
a.insert(16)
a.insert(17)
a.insert(64)
a.insert(6)
a.printll()