# -------- Node Definition --------
class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"Node({self.val})"


# -------- Clone Function (same as LeetCode) --------
def cloneGraph(node):
    if not node:
        return None

    old_to_new = {}

    def dfs(cur):
        if cur in old_to_new:
            return old_to_new[cur]

        copy = Node(cur.val)
        old_to_new[cur] = copy

        for nei in cur.neighbors:
            copy.neighbors.append(dfs(nei))

        return copy

    return dfs(node)


# -------- Helper: Build graph from adjList --------
def build_graph(adjList):
    if not adjList:
        return None

    nodes = [Node(i + 1) for i in range(len(adjList))]

    for i, neighbors in enumerate(adjList):
        for n in neighbors:
            nodes[i].neighbors.append(nodes[n - 1])

    return nodes[0]  # return node 1


# -------- Helper: Convert graph to adjList for printing --------
def graph_to_adjList(node):
    from collections import deque
    visited = set()
    q = deque([node])
    res = {}
    
    while q:
        cur = q.popleft()
        if cur in visited:
            continue
        visited.add(cur)
        res[cur.val] = [n.val for n in cur.neighbors]
        for n in cur.neighbors:
            q.append(n)

    return [res[i] for i in sorted(res)]


# -------- Main --------
if __name__ == "__main__":
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]   # Example input
    original = build_graph(adjList)
    cloned = cloneGraph(original)

    print("Original:", graph_to_adjList(original))
    print("Cloned:  ", graph_to_adjList(cloned))
