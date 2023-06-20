from Node import Node


class LinkedList():
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        cur_node = self.head 
        if cur_node == None:
            self.head = new_node
            return
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)
    
    def show(self):
        cur_node = self.head 
        output = ''
        while cur_node != None:
            output += str(cur_node.get_data) + '-->'
            cur_node = cur_node.get_next()
        print(output)
    
    def len(self):
        counter = 1
        cur_node = self.head 
        while cur_node != None:
            counter += 1
            cur_node = cur_node.get_next()
        print(counter)
    
    def append_start(self, data):
        new_node = Node(data)
        cur_node = self.head 
        new_node.set_data(cur_node)
        self.head = new_node
    
    def remove_last(self):
        while cur_node.get_next().get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(None)






        
    


         