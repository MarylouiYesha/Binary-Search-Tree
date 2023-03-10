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
                return self.left.search(val)
            else:
                return False
        if val > self.value:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.value)

        return elements

    def pre_order_traversal(self):
        elements = [self.value]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def delete(self, val):
        if val < self.value:
            if self.left:
                self.left = self.left.delete(val)
                
        elif val > self.value:
            if self.right:
                self.right = self.right.delete(val)
                
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.value = max_val
            self.left = self.left.delete(max_val)

        return self 

    def find_max(self):
        if self.right is None:
            return self.value
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.value
        return self.left.find_min()


def build_tree(elements):
    root=Node(elements[0])

    for i in range (1, len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__=='__main__':
    nameletters=input("Input Name:")

    
    nameletters_tree=build_tree(nameletters)

    print("Input Letters:",nameletters)
    print("Max:",nameletters_tree.find_max())
    print("Min:",nameletters_tree.find_min())

    search_letter=input("Input Search Letter:")
    print("Search Letter:",nameletters_tree.search(search_letter))

    print("In Order Traversal:",nameletters_tree.in_order_traversal())
    print("Post Order Traversal:",nameletters_tree.post_order_traversal())
    print("Pre Order Traversal",nameletters_tree.pre_order_traversal())

    del_letter=input("Delete Letter:")
    nameletters_tree.delete(del_letter)
    print("After Deleting:",nameletters_tree.in_order_traversal())
    