# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        try:
            h = head
            t = head.next
            while t is not h:
                h = h.next
                t = t.next.next
            return True
        except:
            return False