# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        mp = defaultdict(int)
        index = 0
        temp1 = temp2 = head

        while temp1:
            mp[index] = temp1.val
            temp1 = temp1.next
            index += 1

        start = 0
        index -= 1
        while start <= index:
            temp2.val = mp[start]
            start += 1
            temp2 = temp2.next

            if temp2:
                temp2.val = mp[index]
                index -= 1
                temp2 = temp2.next

        