class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # if I manually literate through the arr
        # will have time limit exceed
        count = Counter(tasks) 
        maxheap =[-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        q =deque() # count, next available time
        time = 0
        while maxheap or q:
            time+=1
            if not maxheap:
                time = q[0][1]
            else:
                cnt = 1+heapq.heappop(maxheap)
                if cnt!=0:
                    q.append([cnt,time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time