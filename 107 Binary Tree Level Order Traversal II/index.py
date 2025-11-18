class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        from collections import deque
        queue = deque([root])
        result = []

        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        # Reverse the result for bottom-up order
        return result[::-1]
