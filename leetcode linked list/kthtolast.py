from linked_list import LinkedList
def nth_to_last(ll,n):
    p1=ll.head
    p2=ll.head
    for i in range(n):
        if p2 is None:
            return None
        p2=p2.next
    while p2:
        p1=p1.next
        p2=p2.next
    return p1
custom_ll=LinkedList()
custom_ll.generate(10,0,99)
print(custom_ll)
print(nth_to_last(custom_ll,3))