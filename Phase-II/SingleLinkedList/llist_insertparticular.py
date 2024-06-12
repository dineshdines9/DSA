# class llist:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next
# def insert(head,data,pos):
#     if pos == 1:
#         node = llist(data)
#         node.next = head
#         return node
#     elif pos == 3:
#         while head.next != None:
#             head = head.next
#         head.next = llist(data)   
#     elif pos == 2:
#         k = 1
#         while head.next!=None & k<pos:
#             head = head.next
#             k+=1
#         head.next = llist(data,head.next)
# head = None
# nums = []
# n = int(input('Enter size :'))
# for i in range(n):
#     nums.append(i)
# # nums = [10,20,30,40,50]
# for i in nums:
#     head = insert(head,i,1)
# def printllist(head):
#     while head != None:
#         print(head.data)
#         head = head.next
# printllist(head)
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
        while temp != None:
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
        while temp.next != None:
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
            k = 1
            temp = self.head
            while temp.next != None and k < pos :
                temp = temp.next
                k += 1
            temp.next = node(data,temp.next)
    def printll(self):
        temp = self.head
        while temp.next != None:
            print(temp.data)
            temp = temp.next
        print(temp.data)
a = llist()
b = llist()
a.insert_end(16)
a.insert_end(17)
a.insert_end(64)
a.insert_end(6)
b.insert_begin(16)
b.insert_begin(17)
b.insert_begin(64)
b.insert_begin(6)
a.insert_position(78,2)
b.insert_position(87,5)
a.printll()
print('-----')
b.printll()