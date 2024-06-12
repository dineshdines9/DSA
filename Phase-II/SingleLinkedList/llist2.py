class llist:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
def insertatbegin(head,data):
    node = llist(data)
    node.next = head
    return node
def insertatend(head,data):
    while head.next != None :
        head = head.next
    head.next = llist(data)
def printllist(head):
    while head != None:
        print(head.data)
        head=head.next
head = llist(1)
# insertatend(head,2)
# insertatend(head,3)
# insertatend(head,4)
head = insertatbegin(head,2)
head = insertatbegin(head,3)
head =insertatbegin(head,4)
printllist(head)



    
     