from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        edges = defaultdict(dict)
        all_prefixes = defaultdict(set)
        inf = 2<<63; maxx = len(source)
        for a,b,c in zip(original, changed, cost):
            all_prefixes[a[0]].add(a)
            edga = edges[a]
            if b not in edga or edga[b] > c:
                edga[b] = c

        all_costs = {}
        def get_cost(src, tgt):
            if src in all_costs:
                return all_costs[src].get(tgt, inf)
            
            #dijkstra but for phrases
            costs = {src:0}; heap = []; heappush(heap, (0, src))
            while heap:
                cost, node = heappop(heap)
                if costs[node] == cost:
                    for nextnode, fee in edges[node].items():
                        nextcost = cost + fee
                        if nextnode not in costs or nextcost < costs[nextnode]:
                            if nextnode not in costs or costs[nextnode] > nextcost:
                                costs[nextnode] = nextcost
                                heappush(heap, (nextcost, nextnode))
            all_costs[src] = costs
            return all_costs[src].get(tgt, inf)

        dp = [inf] * maxx + [0]
        for x in range(maxx-1,-1,-1):
            tail = source[x:]
            head = tail[0]
            res = dp[x+1] if head == target[x] else inf

            for prefix in all_prefixes.get(head, []):
                if not tail.startswith(prefix):
                    continue
                endp = len(prefix) + x
                cur = dp[endp]
                if cur >= inf:
                    continue
                tgt = target[x:endp]
                cur += get_cost(prefix, tgt)
                if cur < res:
                    res = cur
            dp[x] = res
        
        if dp[0]<inf:
            return dp[0]
        return -1