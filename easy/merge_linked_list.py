# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        dummy_list = ListNode()
        head = dummy_list
        
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                # update list1 pointer
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            
            # update head pointer
            head = head.next
        
        # there might be cases where there's 1 list is longer than the other resulting in leftover nodes
        if list1:
            head.next = list1
        elif list2:
            head.next = list2
        
        return dummy_list.next

list1 = [1,2,4]
list2 = [1,3,4]

sol = Solution()
print(sol.mergeTwoLists(list1, list2))