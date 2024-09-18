from linked_list import LinkedList,Node
def intersection(ll1,ll2):
    if ll1.tail is not ll2.tail:
        return False
    shorter=ll1 if len(ll1)<len(ll2) else ll2
    longer=ll2 if len(ll1)<len(ll2) else ll1
    diff=len(longer)-len(shorter)
    shorter_node=shorter.head
    longer_node=longer.head
    for i in range(diff):
        longer_node=longer_node.next
    while shorter_node is not longer_node:
        shorter_node=shorter_node.next
        longer_node=longer_node.next
    return longer_node
def add_same_node(ll1,ll2,value):
    temp=Node(value)
    ll1.tail.next=temp
    ll1.tail=ll1.tail.next
    ll2.tail.next=temp
    ll2.tail=ll2.tail.next
ll1=LinkedList()
ll2=LinkedList()
