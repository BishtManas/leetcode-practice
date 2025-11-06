import heapq

class PowerGrid:
    def __init__(self, c, connections):
        self.c = c
        self.parent = list(range(c + 1))
        self.size = [1] * (c + 1)
        self.online = [True] * (c + 1)

        def find(x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x
        self.find = find

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
        self.union = union

        # Build DSU
        for u, v in connections:
            union(u, v)

        # Build heaps for each component
        self.comp = {}
        for node in range(1, c + 1):
            root = find(node)
            if root not in self.comp:
                self.comp[root] = []
            heapq.heappush(self.comp[root], node)

    def process(self, queries):
        ans = []
        for t, x in queries:
            root = self.find(x)
            if t == 1:
                if self.online[x]:
                    ans.append(x)
                else:
                    heap = self.comp[root]
                    while heap and not self.online[heap[0]]:
                        heapq.heappop(heap)
                    ans.append(heap[0] if heap else -1)
            else:
                self.online[x] = False
        return ans


# Example usage
if __name__ == "__main__":
    c = 5
    connections = [[1,2],[2,3],[3,4],[4,5]]
    queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

    grid = PowerGrid(c, connections)
    print(grid.process(queries))
