# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        odd = head
        even = head.next
        even_start = head.next
        
        while odd.next and odd.next.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        odd.next = even_start
        return head