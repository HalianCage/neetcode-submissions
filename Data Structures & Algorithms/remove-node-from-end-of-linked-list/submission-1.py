# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        second = ListNode()
        second.next = head
        first = head
        index = 0

        while first:

            if index >= n:
                second = second.next
            
            first = first.next
            index += 1

        if index == n:
            head = head.next
            return head

        second.next = second.next.next

        return head


        