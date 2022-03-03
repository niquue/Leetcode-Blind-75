class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f



         #    a
         #   / \
         #  b   c
         # / \   \
         #d  e    f



# Depth-First traversal
# Using iterative solution - with stack
def depth_first(root):

    if root is None:
        return []

    stack = [root]
    depth_order = []
    while stack:
        current = stack.pop()
        depth_order.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return depth_order


result = depth_first(a)
print("depth first: ", result)

# Recursive solution  for depth first
def recursive_depth_first(root):
    if root is None:
        return []

    left_values = recursive_depth_first(root.left)
    right_values = recursive_depth_first(root.right)
    return [root.val, *left_values, *right_values]


result = recursive_depth_first(a)
print(result)


# Breadth first version of tree
def breadth_first(root):
    if root is None:
        return []

    values = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        values.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return values

result = breadth_first(a)
print("breadth first: ", result)


def tree_includes(root, target):
    """
    :param root:
    :param target:
    :return: Boolean, if target exist in tree, will return True, otherwise False
    """
    if root is None:
        return False

    # Breadth-First version first:
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.val == target:
            return True

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False


result = tree_includes(a, "e")
print(result)


def includes_recursive(root, target):
    """
    Recursive version of includes() method for finding if value exists in tree
    :param root:
    :param target:
    :return: Boolean, if target exist in tree, will return True, otherwise False
    """

    if root is None:
        return False
    if root.val == target:
        return True

    return includes_recursive(root.left, target) or includes_recursive(root.right, target)


result = includes_recursive(a, "e")
print(result)
result = includes_recursive(a, "p")
print(result)