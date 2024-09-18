import random
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def _iter__(self):
        temp=self.head
        while temp:
            yield temp
            temp=temp.next
    def __str__(self) -> str:
        temp=self.head
        result=''
        while temp:
            result+=str(temp.value)
            temp=temp.next
            if temp:
                result+=' -> '
        return result
    def __len__(self):
        temp=self.head
        length=0
        while temp:
            length+=1
            temp=temp.next
        return length
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        return self
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        return self
    def generate(self,n,min,max):
        self.head=None
        self.tail=None
        for i in range(n):
            self.append(random.randint(min,max))
        return self

custom_ll=LinkedList()
custom_ll.generate(5,0,100)
print(custom_ll)