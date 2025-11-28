# LeetCode solution
class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        from collections import deque
        q = deque([root])
        result = []

        while q:
            level_size = len(q)
            rightmost = None

            for _ in range(level_size):
                node = q.popleft()
                rightmost = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(rightmost)

        return result
