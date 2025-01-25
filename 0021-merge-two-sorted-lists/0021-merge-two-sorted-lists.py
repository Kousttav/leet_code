class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        new_list = ListNode()
        start = new_list

        while list1 and list2:
            if list1.val <= list2.val:
                start.next = list1
                list1 = list1.next
            else:
                start.next = list2
                list2 = list2.next
            start = start.next
        if list1:
            start.next = list1
        elif list2:
            start.next = list2

        return new_list.next
