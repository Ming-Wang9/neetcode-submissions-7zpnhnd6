class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = {}
        res =[]
        
        for i,v in enumerate(s):
            lastindex[v] = i
        size,r = 0,0
        for i, c in enumerate(s):
            size += 1
            r = max(r, lastindex[c])
            if i == r:
                res.append(size)
                size =0
        return res
                


            