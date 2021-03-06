"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

    Input: root = [2,1,3]
Output: true


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):

    if not root:
        return True

    order = []
    def inOrder(root, order):
        if root is None:
            return
        inOrder(root.left, order)
        order.append(root.val)
        print(root.val)
        inOrder(root.right, order)
    inOrder(root, order)
    print(order)
    for i in range(1, len(order)):
        if order[i] <= order[i-1]:
            return False
    return True


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
# root = TreeNode(5)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(6)

isValidBST(root)