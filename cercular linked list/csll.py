class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)

class CSlinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node:
            result+=str(temp_node.value)
            temp_node=temp_node.next
            if temp_node==self.head:
                break
            result+='-> '
        return result
    
    def append(self,value):

        new_node=Node(value)
        if self.length==0:
            new_node.next=new_node
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length+=1
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            new_node.next=new_node
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.tail.next=new_node
            self.head=new_node
        self.length+=1
    def insert(self,index,value):
        new_node=Node(value)
        if index==0:
            return self.prepend(value)
        elif index==self.length:
            return self.append(value)
        elif index<0 or index>self.length:
            raise Exception('index is out of range')
        else:
            temp_node=self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            nxt=temp_node.next
            new_node.next=nxt
            temp_node.next=new_node
        self.length+=1
    def traverse(self):
        temp_node=self.head
        while temp_node:
            print(temp_node.value)
            temp_node=temp_node.next
            if temp_node==self.head:
                break
        return self
    def search(self,target):
        temp_node=self.head
        while temp_node:
            if temp_node.value==target:
                return True
            temp_node=temp_node.next
            if temp_node==self.head:
                break
        return False
    
    def get(self,index):
        if index==-1:
            return self.tail
            
        elif index<-1 or index>=self.length:
            return None
        
        else:
            temp_node=self.head
            for _ in range(index):
                temp_node=temp_node.next
            return temp_node
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    def pop_first(self):
        if self.length==0:
            return None
        temp_node=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head
            temp_node.next=None
        self.length-=1
        return temp_node

    def pop(self):
        if self.length==0:
            return None
        temp_node=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            temp.next=self.head
            self.tail=temp
            temp_node.next=None
        self.length-=1
        return temp_node

csll=CSlinkedList()
csll.append(10)
csll.append(20)
csll.prepend(5)
print(csll)
csll.insert(0,100)
print(csll)
csll.traverse()
print(csll.search(10))
print(csll.get(0))
csll.set_value(0,200)
print(csll)
csll.pop_first()
print(csll)
csll.pop()
print(csll)
   
    