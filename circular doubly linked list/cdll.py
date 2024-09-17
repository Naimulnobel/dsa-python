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
  
    def search(self,target):
        temp=self.head

        while temp:
            if temp.value==target:
                return True
            temp=temp.next
            if temp==self.head:
                break
        return False
    def get(self,index):
        
        if index<0 or index>=self.length:
            return None
        temp=None
        if index<self.length//2:
            temp=self.head
            for i in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for i in range(self.length-1,index,-1):
                temp=temp.prev
        return temp
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        new_node.prev=temp
        temp.next.prev=new_node
        temp.next=new_node
        self.length+=1
        return True
    def pop_first(self):
        

        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=temp.next
            temp.next=None
            temp.prev=None
            self.head.prev=self.tail
            self.tail.next=self.head
            self.length-=1
            return temp

    def pop(self):
        if self.length==0:
            return None
        temp=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=temp.prev
            self.tail.next=self.head
            self.head.prev=self.tail
            temp.next=None
            temp.prev=None
            self.length-=1
            return temp
    def remove(self,index):
        if index<0 or index>self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        temp=self.get(index)
        temp.prev.next=temp.next
        temp.next.prev=temp.prev
        temp.next=None
        temp.prev=None
        self.length-=1
        return temp
    def delete_all(self):
        if self.length==0:
            return None
        else:
            self.head=None
            self.tail=None
            self.length=0
            return self
        
cdll=CDoublyLinkedList()
cdll.append(23)
cdll.append(34)
cdll.append(45)
# cdll.traverse()
print('-------------------')
cdll.reverse_traverse()
# print('-------------------')
print(cdll)
# print(cdll.get(2))
# print(cdll)
print('-------------------')
cdll.pop()
cdll.pop_first()
print(cdll)