from linked_list import LinkedList

def sum_list(ll1,ll2):
    n1=ll1.head
    n2=ll2.head
    carry=0
    ll=LinkedList()
    while n1 or n2:
        result=carry
        if n1:
            result+=n1.value
            n1=n1.next
        if n2:
            result+=n2.value
            n2=n2.next
        ll.append(result%10)
        carry=result//10
    
    return ll
ll1=LinkedList()
ll2=LinkedList()
ll1.append(7)
ll1.append(1)
ll1.append(6)
ll2.append(5)
ll2.append(9)
ll2.append(2)
print(ll1)
print(ll2)
print(sum_list(ll1,ll2))