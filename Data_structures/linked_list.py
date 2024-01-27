class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None
class LinkedList():
    def __init__(self):
        self.head = None
    
    def append_node(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next_node is not None:
                current = current.next_node

            current.next_node = new_node
            
    def display_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next_node
        print('None')
            
some_list = LinkedList()

some_list.append_node(1)

some_list.append_node(2)

some_list.append_node(3)

some_list.display_list()