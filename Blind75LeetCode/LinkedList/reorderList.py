"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Input: head = [1,2,3,4]
Output: [1,4,2,3]


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):

    if head is None and head.next is None:
        return None

    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    cur = slow.next
    prev = None
    while cur:
        temp = cur.next
        print(temp.val)
        cur.next = prev
        prev = cur
        cur = temp
    slow.next = None

    head1, head2 = head, prev
    while head2:
        temp = head1.next
        head1.next = head2
        head1 = head2
        head2 = temp
    # get_vals = []
    # cur = head.next
    # while cur:
    #     get_vals.append(cur.val)
    #     cur = cur.next
    #
    # cur = head.next
    # flag = False
    # while cur:
    #     if not flag:
    #         cur.val = get_vals.pop()
    #         cur = cur.next
    #         flag = True
    #     else:
    #         cur.val = get_vals.pop(0)
    #         cur = cur.next
    #         flag = False
    # return head


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
one.next = two
two.next = three
three.next = four
four.next = five
reorderList(one)