# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        def check(node):
            if not node:
                return 0  # height of empty tree is 0

            left = check(node.left)
            if left == -1:
                return -1  # left subtree not balanced

            right = check(node.right)
            if right == -1:
                return -1  # right subtree not balanced

            if abs(left - right) > 1:
                return -1  # current node not balanced

            return max(left, right) + 1  # return height

        return check(root) != -1

# -----------------------------
# Sample tree: [3,9,20,null,null,15,7]
# This is a balanced binary tree

# Creating the tree manually
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Create Solution object and test
sol = Solution()
print("Is tree balanced?", sol.isBalanced(root))  # Output: True
