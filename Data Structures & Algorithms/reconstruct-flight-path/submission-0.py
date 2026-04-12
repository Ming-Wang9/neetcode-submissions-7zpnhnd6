class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {src :[] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            graph[src].append(dst)
        res = ['JFK']
        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            if src not in graph:
                return False
            temp = list(graph[src])
            for i, nei in enumerate(temp):
                graph[src].pop(i)
                res.append(nei)
                if dfs(nei):
                    return True
                else:
                    graph[src].insert(i,nei)
                    res.pop()
            return False
        dfs('JFK')
        return res




