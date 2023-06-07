# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        tail,size = head,1
        while tail.next:
            size+=1
            tail = tail.next
        k = k%size
        if k == 0:
            return head
        curr = tail.next = head
        size = size - (k) - 1
        for i in range(0,size):
           curr  = curr.next
        newHead = curr.next
        curr.next = None
        return newHead
        