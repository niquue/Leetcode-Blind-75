class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev



linked_list = [1, 2, 3, 4, 5]
node = ListNode(0)
length = 0
cur = node
while cur.next is None and length < len(linked_list):
    cur.next = ListNode(linked_list[length])
    length += 1
    cur = cur.next

result = reverseList(node.next)
while result:
    print(result.val)
    result = result.next