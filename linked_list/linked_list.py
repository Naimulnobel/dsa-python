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
    
    





my_linked_list=LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.prepend(0)
my_linked_list.insert(1,3)
print(my_linked_list)