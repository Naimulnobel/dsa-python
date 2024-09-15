class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)
    
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def __str__(self):
        temp=self.head
        result=''
        while temp:
            result+=str(temp.value)
            
            if temp.next:
                result+='<-->'
            temp=temp.next
        return result
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return self 

    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return self
    def reverse_traverse(self):
        temp=self.tail
        while temp:
            print(temp.value)
            temp=temp.prev
        return self
    def search(self,value):
        temp=self.head
        index=0
        while temp:
            if temp.value==value:
                return index
            temp=temp.next
            index+=1
        return -1
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        if index<self.length//2:
            temp=self.head
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    def insert(self,index,value):
        new_node=Node(value)
        if index==0:
            return self.prepend(value)
        elif index==self.length:
            return self.append(value)
        elif index<0 or index>self.length:
            raise Exception('index is out of range')
        else:
            temp_node=self.get(index-1)
            new_node.next=temp_node.next
            temp_node.next=new_node
            new_node.prev=temp_node
            new_node.next.prev=new_node
        self.length+=1
        return self
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=temp.next
            self.head.prev=None
            temp.next=None
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
            self.tail.next=None
            temp.prev=None
        self.length-=1
        return temp
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        elif index==self.length-1:
            return self.pop()
        else:
            temp=self.get(index-1)
            temp_node=temp.next
            temp.next=temp_node.next
            temp_node.next.prev=temp
            temp_node.next=None
            temp_node.prev=None
        self.length-=1
        return temp_node
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        elif index==self.length-1:
            return self.pop()
        else:
            temp=self.get(index)
            temp.prev.next=temp.next
            temp.next.prev=temp.prev
            temp.next=None
            temp.prev=None
            
        self.length-=1
        return temp

new_list=DoublyLinkedList()
new_list.append(1)
new_list.append(2)
new_list.append(3)
new_list.prepend(0)
print(new_list)
# new_list.reverse_traverse()
# print(new_list.search(2))
print(new_list.get(1))
