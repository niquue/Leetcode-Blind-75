"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

def kthSmallest(root, k):
    nodes = []
    def get_node_vals(node):
        if not node:
            return

        nodes.append(node.val)
        get_node_vals(node.left)
        get_node_vals(node.right)
    get_node_vals(root)
    nodes.sort()
    return nodes[k-1]