import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        def gain(passi, totali):
            
            return (passi + 1) / (totali + 1) - passi / totali

        heap = []
        for passi, totali in classes:
            
            heapq.heappush(heap, (-gain(passi, totali), passi, totali))
        
        for _ in range(extraStudents):
            g, passi, totali = heapq.heappop(heap)
            passi += 1
            totali += 1
            heapq.heappush(heap, (-gain(passi, totali), passi, totali))

        total_ratio = sum(passi / totali for _, passi, totali in heap)
        return total_ratio / len(classes)

sol = Solution()
print(sol.maxAverageRatio([[1,2],[3,5],[2,2]], 2))  # Output: 0.78333
print(sol.maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4))  # Output: 0.53485
