# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        
        while head:
            newNode = ListNode()
            newNode.val = head.val
            newNode.next = result
            result = newNode
            head = head.next    
        return result