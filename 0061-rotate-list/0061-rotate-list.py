# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l,size = head,1
        if l:
            while l.next:
                size+=1
                l = l.next
            l.next,l = head,head 
            size = size - (k%size) - 1
            while size:
                size-=1
                l = l.next
            head = l.next
            l.next = None
        return head
        