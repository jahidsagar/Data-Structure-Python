class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        # if i dont assign value, then it will make issue in while loop
        self.head = Node(-1)
        self.tail = self.head
    
    def insert_at_first(self, value):
        new_node = Node(value=value)
        new_node.next = self.head.next
        self.head.next = new_node
    
    def insert_at_end(self, value):
        self.tail.next = Node(value=value)
        self.tail = self.tail.next

    def show(self):
        temp = self.head.next
        while temp:
            print(temp.value)
            temp = temp.next

ll = LinkedList()
ll.insert_at_end(4)
ll.insert_at_first(5)
ll.insert_at_end(6)
ll.show()