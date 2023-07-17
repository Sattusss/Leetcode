# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            
            def convert_to_number(head):
                num = 0
                while head:
                    num = num * 10 + head.val
                    head = head.next
                return num
            
            def convert_to_list(num):
                if num == 0:
                    return ListNode(0)
                head = None
                while num:
                    head = ListNode(num % 10, head)
                    num //= 10
                return head
            
            return convert_to_list(convert_to_number(l1) + convert_to_number(l2))
    