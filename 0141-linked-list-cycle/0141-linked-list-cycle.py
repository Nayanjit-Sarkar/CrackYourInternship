# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l,add = head,{}
        while l:
            if l not in add:
                add[l] = l.val
                l = l.next
            else:
                return True
        return False
