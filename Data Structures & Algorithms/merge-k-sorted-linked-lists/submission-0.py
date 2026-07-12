# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode(float('-inf'))

        while lists:
            temp1 = dummy
            temp2 = lists.pop()
            if temp2.next:
                lists.append(temp2.next)

            while temp1.next and temp1.next.val < temp2.val:
                temp1 = temp1.next

            temp3 = temp1.next
            temp1.next = temp2
            temp2.next = temp3

        return dummy.next

        