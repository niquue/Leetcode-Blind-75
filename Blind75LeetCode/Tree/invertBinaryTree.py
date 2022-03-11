"""
Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):

    if not root:
        return None

    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)


four = TreeNode(4)
four.left = TreeNode(2)
four.left.left = TreeNode(1)
four.left.right = TreeNode(3)

four.right = TreeNode(7)
four.right.left = TreeNode(6)
four.right.right = TreeNode(9)
