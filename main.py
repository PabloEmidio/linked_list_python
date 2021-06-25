class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
        
    def __len__(self):
        return len(self.to_list())
    
    
    def __str__(self):
        return f'{self.to_list()}'
    
    
    def __getitem__(self, index):
        return self.to_list()[index]
    
    
    def __add__(self, data):
        self.append(data)
    
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        return

        
    def pop(self):
        node = self.head
        while node.next.next != None:
            node = node.next
        last_data = node.next.data
        node.next = None
        return last_data
        
        
    def index(self, index):
        node = self.head
        to_increment = 0
        while node:
            if node.data==index:
                return to_increment
            node = node.next
            to_increment+=1
        raise ValueError(f'{index} is not in linked list')

    
    def to_list(self):
        node = self.head
        node_data = [node.data]
        while node.next:
            node = node.next
            node_data.append(node.data)
        return node_data
    
 
