# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = []
        cur = head
        while cur:
            node.append(cur)
            cur = cur.next
        removeInd = len(node) - n
        if removeInd == 0:
            return head.next
        node[removeInd -1].next = node[removeInd].next
        return head
