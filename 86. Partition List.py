# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
            
            # 1. 2 pointers
            # Time O(n), space O(1)
            # dummy = ListNode(-1)
            # dummy.next = head
            # cur = dummy
            # while cur.next and cur.next.val < x:
            #     cur = cur.next
            # pre = cur
            # cur = cur.next
            # while cur and cur.next:
            #     if cur.next.val < x:
            #         temp = cur.next
            #         cur.next = temp.next
            #         temp.next = pre.next
            #         pre.next = temp
            #         pre = pre.next
            #     else:
            #         cur = cur.next
            # return dummy.next
    
            # 2. 2 pointers
            # Time O(n), space O(1)
            dummy1 = ListNode(-1)
            dummy2 = ListNode(-1)
            cur1 = dummy1
            cur2 = dummy2
            cur = head
            while cur:
                if cur.val < x:
                    cur1.next = cur
                    cur1 = cur1.next
                else:
                    cur2.next = cur
                    cur2 = cur2.next
                cur = cur.next
            cur2.next = None
            cur1.next = dummy2.next
            return dummy1.next
    