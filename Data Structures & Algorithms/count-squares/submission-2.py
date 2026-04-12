class CountSquares:
    def __init__(self):
        self.ptsCount = {}
        self.pts = []

    def add(self, point: List[int]) -> None:
        x,y = point
        self.ptsCount[(x, y)] = self.ptsCount.get((x, y), 0) + 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += (
                self.ptsCount.get((x, py), 0) *
                self.ptsCount.get((px, y), 0)
            )
        return res