# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next #Progressed by 2x
            slow = slow.next # Progress by 1

            if fast == slow:
                return True
        return False


        