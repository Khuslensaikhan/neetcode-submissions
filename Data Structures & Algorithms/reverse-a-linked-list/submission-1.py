# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [0 | *] --> [1 | *] --> [2 | *] --> [3 | /]
#  |          |          |          |
# data=0     data=1     data=2     data=3
# next=1     next=2     next=3     next=None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

