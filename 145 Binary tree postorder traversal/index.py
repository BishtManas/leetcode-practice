from typing import Optional, List

# Tree node class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution class with postorder traversal
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push left first so right gets processed first
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]  # Reverse at the end for correct postorder

# Test it
if __name__ == "__main__":
    # Tree: [1, None, 2, 3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    sol = Solution()
    print("Postorder Traversal:", sol.postorderTraversal(root))  # Output: [3, 2, 1]
