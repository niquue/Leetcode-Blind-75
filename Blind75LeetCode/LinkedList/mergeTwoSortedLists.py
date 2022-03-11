"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):

    if list1 and not list2:
        return list1
    if not list1 and list2:
        return list2
    if not list1 and not list2:
        return list1

    dummy = ListNode(0)
    cur = dummy
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            cur = cur.next
            list1 = list1.next
        else:
            cur.next = list2
            cur = cur.next
            list2 = list2.next
    if list1:
        cur.next = list1
    if list2:
        cur.next = list2
    return dummy.next