class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


# --------- Example Tree Creation ---------
# Creating this tree:
#         5
#        / \
#       4   8
#      /   / \
#     11  13  4
#    /  \
#   7    2

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

# --------- Test the Function ---------
target_sum = 22
solution = Solution()
result = solution.hasPathSum(root, target_sum)

print(f"Path with target sum {target_sum} exists:", result)