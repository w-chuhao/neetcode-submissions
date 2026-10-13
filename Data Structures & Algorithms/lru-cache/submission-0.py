class Node:
    def __init__(self,key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}
        self.capacity = capacity

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
        
    def insert(self,node):
        prev = self.right.prev
        self.right.prev = node
        prev.next = node
        node.prev = prev
        node.next = self.right


    
    def delete(self,node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        
        curr = self.mp[key]
        self.delete(curr)
        self.insert(curr)

        return curr.val


    def put(self, key: int, value: int) -> None:

        if key in self.mp:
            curr = self.mp[key]
            curr.val = value

            self.delete(curr)
            self.insert(curr)

            return
        
        node = Node(key,value)
        self.mp[key] = node
        self.insert(node)

        if len(self.mp)>self.capacity:
            node = self.left.next
            self.delete(node)
            self.mp.pop(node.key)


        
