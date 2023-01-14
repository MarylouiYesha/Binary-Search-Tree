class Node:
    def __init__(self, value):
       self.value = value
       self.left = None
       self.right =None 

    def add_child(self,value):
        if value == self.value:
            return
        
        if value < self.value:
            if self.left:
                self.left.add_child(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = Node(value)
                
    def in_order_traversal(self):
        elements=[]

        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.value)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements            
              
def build_tree(elements):
    root=Node(elements[0])

    for i in range (1, len(elements)):
        root.add_child(elements[i])