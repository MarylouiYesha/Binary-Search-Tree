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
              
    
    def search(self,val):
        if self.value == val:
            return True
        if val < self.value:
            if self.left:
                self.left.search(val)
            else:
                return False
        if val > self.value:
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements):
    root=Node(elements[0])

    for i in range (1, len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__=='__main__':
    nameletters=['A','G','F','B']
    nameletters_tree=build_tree(nameletters)
    print(nameletters_tree.in_order_traversal())
    print(nameletters_tree.search('A'))