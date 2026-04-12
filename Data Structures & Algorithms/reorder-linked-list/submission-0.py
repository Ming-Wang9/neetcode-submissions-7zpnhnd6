# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None

        node = []
        cur = head
        while cur:
            node.append(cur)
            cur = cur.next

        l, r = 0, len(node)-1
        while l < r:
            node[l].next = node[r]
            l +=1
            if l == r:
                break
            node[r].next = node[l]
            r -= 1
        node[l].next = None
        

    
        