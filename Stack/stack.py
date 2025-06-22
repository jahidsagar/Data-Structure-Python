# stack using linked list
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
        self.count = 0
    
    def push(self,value):
        self.tail.next = Node(value=value)
        self.tail = self.tail.next
        self.count += 1
    
    def pop(self):
        if self.empty():
            return
        
        temp = self.head
        while temp.next.next:
            temp = temp.next
        self.tail = temp
        self.tail.next = None
        self.count -= 1

    def empty(self):
        if self.count <= 0:
            return True
        return False
    
    # this function is just used for checking values
    def show(self):
        if self.empty():
            return
        
        temp = self.head.next
        while temp:
            print(temp.value)
            temp = temp.next

st = Stack()
st.push(6)
st.push(8)
st.push(10)
st.show()
st.pop()
st.pop()
st.pop()
st.pop()
st.pop()
st.show()

