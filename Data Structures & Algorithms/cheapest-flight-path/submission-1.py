import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], 
                          src: int, dst: int, k: int) -> int:
        
        # Build adjacency list using plain dictionary
        graph = {}
        for s, d, p in flights:
            if s not in graph:
                graph[s] = []
            graph[s].append((d, p))

        # Min-heap: (cost, airport, stops_used)
        minheap = [(0, src, 0)]

        # Store the minimum stops we have seen for each airport
        minstop = {}

        while minheap:
            price, airport, stop = heapq.heappop(minheap)

            if airport == dst:
                return price

            if stop > k:
                continue

            if airport in minstop and minstop[airport] < stop:
                continue

            minstop[airport] = stop

            # airport may have no outgoing flights
            if airport in graph:
                for nxt, p in graph[airport]:
                    heapq.heappush(minheap, (price + p, nxt, stop + 1))

        return -1
