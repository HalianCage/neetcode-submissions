# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast, slow = head, head

        # finding the mid point
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reversing the list
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while prev:
            temp1, temp2 = head.next, prev.next
            head.next = prev
            prev.next = temp1
            head, prev = temp1, temp2
        