class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)
class CDoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def __str__(self):
        temp=self.head
        result=''
        while temp:
            result+=str(temp.value)
            temp=temp.next        
            if temp ==self.head:
                break
            result+=' <-> '
            
        return result
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            self.head.prev=self.tail
            self.tail.next=self.head
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
            self.tail.next=self.head
            self.head.prev=self.tail
        self.length+=1
        return self

    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            self.head.prev=self.tail
            self.tail.next=self.head
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            self.head.prev=self.tail
            self.tail.next=self.head
        self.length+=1
        return self
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next
            if temp==self.head:
                break
        return self
    def reverse_traverse(self):
        temp=self.tail
        while temp:
            print(temp.value)
            temp=temp.prev
            if temp==self.tail:
                break
        return self
  
    
cdll=CDoublyLinkedList()
cdll.append(23)
cdll.append(34)
cdll.append(45)
cdll.traverse()
print('-------------------')
cdll.reverse_traverse()
# print(cdll)