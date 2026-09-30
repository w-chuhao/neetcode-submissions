"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        mp = {}

        curr = head

        while curr:
            new = Node(curr.val)
            mp[curr] = new
            curr = curr.next
        
        curr = head

        while curr:

            new = mp.get(curr)
            nxt = mp.get(curr.next)
            rand = mp.get(curr.random)

            new.next = nxt
            new.random = rand

            curr = curr.next
        
        return mp[head]



        