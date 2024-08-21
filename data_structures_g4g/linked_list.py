# Make a class Node that will hold 'data' and 'next'
class Node:
  def __init__(self, data):
      self.data = data
      self.next = None

# make class to hold 'head' then reference back to class node to insert the data into it
class LinkedMessages:
  def __init__(self):
    self.head = None
    
  def insertAtBegin(self,data):
    new_node =Node(data)
    if self.head is None:
      self.head = new_node
      return
    else: 
      new_node.next = self.head
      self.head = new_node
      
  def insertAtIndex(self,data,index):
    if(index == 0):
      self.insertAtBegin(data)
    position = 0
    current_node = self.head
    while (current_node != None and position+1 != index):
      position = position+1
      current_node = current_node.next
      
    if current_node != None:
      new_node = Node(data)
      new_node.next = current_node.next
      current_node.next = new_node
    else:
      print("Index not present")
  
  def insertAtEnd(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    
    current_node = self.head
    while(current_node.next):
      current_node = current_node.next
      
    current_node.next = new_node
    
  def updateNode(self,value,index):
    current_node = self.head
    position = 0
    if position == index:
      current_node.data = value
    else:
      while(current_node != None and position != index):
        position = position + 1
        current_node = current_node.next
        
      if current_node != None:
        current_node.data = value
      else:
        print("Index not present")
               
  def remove_first_node(self):
    if (self.head == None):
      return
    self.head = self.head.next
    
  def remove_last_node(self):
    if self.head is None:
      return
    
    current_node = self.head
    while(current_node.next != None and current_node.next.next != None):
      current_node = current_node.next
    current_node.next = None
  
  def remove_at_index(self, index):
    if self.head == None:
      return
    
    current_node = self.head
    position = 0
    
    if position == index:
      self.remove_first_node()
    else:
      while(current_node != None and position+1 != index):
        position = position+1
        current_node = current_node.next
        
      if current_node != None:
        current_node.next = current_node.next.next 
      else:
        print("Index not present")
  
  def remove_node(self, data):
    current_node = self.head
    
    if current_node.data == data:
      self.remove_first_node()
      return
    
    while current_node is not None and current_node.next.data != data:
      current_node = current_node.next
      
    if current_node is None:
      return
    else:
      current_node.next = current_node.next.next
      
  def printLL(self):
    current_node = self.head
    while(current_node):
      print(current_node.data)
      current_node = current_node.next
     
  def sizeOfLL(self):
    size = 0
    if(self.head):
      current_node = self.head
      while(current_node):
        size = size+1
        current_node = current_node.next
      return size
    else:
      return 0 
    
link = LinkedMessages()    

link.insertAtEnd('Fellow')
link.insertAtEnd('Lets Code')
link.insertAtBegin('Hello')
link.insertAtEnd('Together')
link.insertAtIndex('Coder', 2)

print("Node Data")
link.printLL()

print("\nRemove First Node")
link.remove_first_node()
print("Remove Last Node")
link.remove_last_node()
print("Remove Node at Index 1")
link.remove_at_index(1)

print("\nLinked list after removing a node:")
link.printLL()

print("\nUpdate node Value")
link.updateNode('Friend', 0)
link.printLL()

print("\nSize of linked list :", end=" ")
print( link.sizeOfLL())