# Define the structure of the tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to check if two binary trees are the same
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and
            isSameTree(p.left, q.left) and
            isSameTree(p.right, q.right))

# -------------- Test Example --------------

# Example 1: Trees are the same
# Tree:       1
#            / \
#           2   3
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

# Run the function and print result
print("Are trees the same?", isSameTree(p, q))  # Output: True
