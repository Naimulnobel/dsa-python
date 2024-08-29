class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+='->'
            temp_node=temp_node.next
        return result
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return self
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return self
    def insert(self,index,value):
        new_node=Node(value)
        temp_node=self.head
        if index==0:
            self.prepend(value)
        elif index>=self.length:
            self.append(value)
        else:
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1
        return self

    def get(self,index):
        if index>=self.length:
            return None
        if index<0:
            return None
        temp_node=self.head
        for _ in range(index):
            temp_node=temp_node.next
        return temp_node

    def set_value(self,index,value):
        temp_node=self.get(index)
        if temp_node:
            temp_node.value=value
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
            temp.next=None
            self.tail=temp
        self.length-=1
        return temp_node
    def remove(self,index):
        if index>=self.length:
            return None
        elif index<0:
            return None
        elif index==0:
            return self.pop_first()
        elif index==self.length-1:
           return self.pop()
       
        prev_node=self.get(index-1)
        popped_node=prev_node.next
        prev_node.next=popped_node.next
        popped_node.next=None
        self.length-=1
        return popped_node
new_list=LinkedList()
new_list.append(1)
print(new_list)
new_list.prepend(0)
print(new_list)
new_list.insert(0,2)
print(new_list)
new_list.get(0)
new_list.get(1)
print(new_list)
new_list.set_value(1,3)
print(new_list)
new_list.pop_first()
print(new_list)
new_list.pop()
print(new_list)
new_list.remove(0)
print(new_list)
            