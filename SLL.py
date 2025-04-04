#Creating a node
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
#Node1=Node(10)
#print(Node1.data)
#print(Node1.ref)
        
class SinglyLL:
    def __init__(self):
        self.head=None
        