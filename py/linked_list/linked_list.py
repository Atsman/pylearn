class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, value, position):
        new_node = Node(value)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        pos = 0
        prev = None
        current = self.head
        while current and pos < position:
            pos += 1
            prev = current
            current = current.next
            
        if pos != position:
            raise Exception("Ll last index: {}, but {} needed".format(pos, position))
            
        prev.next = new_node
        new_node.next = current
            
        
    def prepend(self, value):
        self.insert(value, 0)
    
    def append(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            return
            
        last_node = self.last()
        last_node.next = new_node

    def delete(self, position):
        if position == 0:
            self.head = self.head.next
            return

        node = self.get(position - 1)
        node.next = node.next.next

    def get(self, position):
        pos = 0
        current = self.head

        while current and pos < position:
            pos += 1
            current = current.next

        return current
        
    def last(self):
        current = self.head
        
        if not current:
            return None
        
        while current.next:
            current = current.next
            
        return current
        
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def to_list(self):
        res = []
        current = self.head
        while current:
            res.append(current.value)
            current = current.next
        return res
