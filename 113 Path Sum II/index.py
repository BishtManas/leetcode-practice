class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, current_path, current_sum):
            if not node:
                return

            current_path.append(node.val)
            current_sum += node.val

            # If leaf and sum matched → store the path
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(current_path))

            # Go left and right
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)

            # Backtrack
            current_path.pop()

        dfs(root, [], 0)
        return result