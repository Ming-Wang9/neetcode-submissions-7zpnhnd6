class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indx = {}
        for i,c in enumerate(s):
            indx[c] = i
        res =[]
        size =0
        lastindx =0
        for i,c in enumerate(s):
            size+=1
            lastindx=max(lastindx, indx[c])
            if i == lastindx:
                res.append(size)
                size = 0
        return res