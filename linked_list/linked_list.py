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
        output=''
        while temp_node is not None:
            output+=str(temp_node.value)
            if temp_node.next is not None:
                output+='->'
            temp_node=temp_node.next
        return output
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
                print(temp_node.value)
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1
        return self
    def traverse(self):
        temp_node=self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node=temp_node.next
        return self
    def search(self,value):
        temp_node=self.head
        index=0
        while temp_node is not None:
            if temp_node.value==value:
                
                return index
            temp_node=temp_node.next
            index+=1
        return -1
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
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
           while temp.next is not self.tail:
               temp=temp.next
           temp.next=None
           self.tail=temp
        self.length-=1
        return temp_node
    def remove(self,index):
        if index>=self.length:
            return None
        if index<0:
            return None
        if index==0:
            self.head=self.head.next
        else:
            prev_node=self.get(index-1)
            popped_node=prev_node.next
            prev_node.next=popped_node.next
            popped_node.next=None
        self.length-=1
        return popped_node
    def delete_all(self):
        self.head=None
        self.tail=None
        self.length=0   
        return self






my_linked_list=LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.prepend(0)
print(my_linked_list)
my_linked_list.insert(1,3)

my_linked_list.traverse()

my_linked_list.pop_first()
print(my_linked_list)