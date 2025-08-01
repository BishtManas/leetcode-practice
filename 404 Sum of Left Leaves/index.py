class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        def isLeaf(node):
            return node and not node.left and not node.right

        def dfs(node):
            if not node:
                return 0
            total = 0
            if isLeaf(node.left):
                total += node.left.val
            total += dfs(node.left)
            total += dfs(node.right)
            return total

        return dfs(root)

# 🔧 Example Tree: [3, 9, 20, None, None, 15, 7]
# Create the tree structure
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# ✅ Run the solution
sol = Solution()
print("Sum of Left Leaves:", sol.sumOfLeftLeaves(root))  # Output should be 24
