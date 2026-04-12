class CountSquares:

    def __init__(self):
        self.ptCount = {}
        self.pt = []
    def add(self, point: List[int]) -> None:
        x,y = point[0], point[1]
        self.ptCount[(x,y)] = 1+ self.ptCount.get((x,y), 0)
        self.pt.append([x,y])
    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point[0], point[1]
        for x, y in self.pt:
            if (abs(px-x) != abs(py-y) or px==x or py==y):
                continue
            res+=self.ptCount.get((px,y), 0) * self.ptCount.get((x,py), 0)
        return res
        
