# class llist:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next
# def insert(head,data):
#     node = llist(data)
#     node.next = head
#     return node
# def printllist(head):
#     while head != None:
#         print(head.data)
#         head = head.next   
# head = llist(1)
# head = insert(head,2)
# head = insert(head,3)
# head = insert(head,4)
# printllist(head)
class node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class llist:
    def __init__(self,head=None):
        self.head = head
    def insert(self,data):
        self.head = node(data,self.head)
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