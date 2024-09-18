from linked_list import LinkedList
def partition(ll,x):
    current=ll.tail=ll.head
    while current:
        next_node=current.next
        current.next=None
        if current.value<x:
            current.next=ll.head
            ll.head=current
        else:
            ll.tail.next=current
            ll.tail=current
        current=next_node
    if ll.tail.next is not None:
        ll.tail.next=None
custom_ll=LinkedList()
custom_ll.generate(5,0,50)

partition(custom_ll,10)
print(custom_ll)