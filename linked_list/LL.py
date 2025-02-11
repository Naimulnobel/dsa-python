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
       
        if index==0:
            self.prepend(value)
        elif index>=self.length:
            self.append(value)
        else:
            new_node=Node(value)
            temp_node=self.head
            for _ in range(index-1):
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

            
        
    

ll=LinkedList()
print(ll.append(2))
print(ll.prepend(1))
print(ll.traverse())
print(ll.search(2))