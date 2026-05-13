# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = tail = ListNode() 

        while list1 and list2: #while both lists have nodes:
            if list1.val < list2.val: #compare
                tail.next = list1 #attach the smaller node to tail.next
                list1 = list1.next #move forward
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return mergedList.next

            



            
        