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
        _map = {}
        curr = head
        while curr:
            cop_node = Node(curr.val)
            _map[curr] = cop_node
            curr = curr.next
        
        curr = head

        while curr:
            new_curr = _map[curr]

            new_curr.next = _map.get(curr.next)
            new_curr.random = _map.get(curr.random)

            curr = curr.next

        return _map[head]



        
