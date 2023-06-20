class Node():
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next
    
    #get metods 
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next 
    
    #set metods
    def set_data(self, data):
        self.data = data 

    def set_next(self, next):
        self.next = next
        
        