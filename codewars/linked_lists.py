class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def printtraverse(head):
    currentnode = head
    
    while currentnode:
        print(currentnode.data, end=' -> ')
        currentnode = currentnode.next
    
node1 = Node(1)
node2 = Node(3)
node3 = Node(7)
node4 = Node(2)
node5 = Node(9)
node6 = Node(4)
 
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
  
printtraverse(node1)