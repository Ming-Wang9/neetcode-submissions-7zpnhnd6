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
        copy_linklist = {None:None}
        cur = head
        while cur: 
            copy_node = Node(cur.val)
            copy_linklist[cur]= copy_node
            cur = cur.next
        cur = head
        while cur:
            copy_node = copy_linklist[cur]
            copy_node.next = copy_linklist[cur.next]
            copy_node.random = copy_linklist[cur.random]
            cur = cur.next
        return copy_linklist[head]

        