from typing import Optional

# ✅ Definition of the binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ✅ Solution class with the minDepth function
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return min(left, right) + 1

# ✅ Example usage:
if __name__ == "__main__":
    # Build this binary tree:
    #         1
    #        / \
    #       2   3
    #      /
    #     4

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    # Create solution object and call the function
    sol = Solution()
    print("Minimum depth:", sol.minDepth(root))  # Output: 2 (via right node 3)
