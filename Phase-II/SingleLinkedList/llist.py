class llist():
    def __init__(self,data,next=None) -> None:
        self.data = data
        self.next = next
# a = llist(2)
# a.next = llist(3)
# a.next.next= llist(4)
# def printllist(head):
while(a != None):
    print(a.data)
    a = a.next
# printllist(head)