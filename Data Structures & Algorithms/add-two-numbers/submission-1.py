# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def todigit(l):
            if not l:
                return 0
            cur = l
            res = ''
            while cur:
                res = str(cur.val)+res
                cur = cur.next
            return res
        d1 = int(todigit(l1))
        d2 = int(todigit(l2))
        s = str(d1+d2)
        dummy = ListNode(0)
        cur = dummy
        for c in s:
            cur.next = ListNode(c)
            cur = cur.next
        pre = None
        cur = dummy.next
        while cur:
            temp=cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
