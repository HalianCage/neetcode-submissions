# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        '''
        ALGORITHM:-
        Step 1: get length of LL by traversing it
        Step 2: Calculate the target position from start by len-n+1
        Step 3: Start traversing once again, on reaching one node before the position, bypass the node
        Step 4: Return the head
        '''

        length = 0

        temp = head
        while temp:
            length += 1
            temp = temp.next

        target_pos = length - n

        if target_pos == 0:
            head = head.next
            return head

        temp = head
        index = 0

        while temp:
            index += 1
            if index == target_pos:
                temp.next = temp.next.next
                return head
            temp = temp.next
        
        