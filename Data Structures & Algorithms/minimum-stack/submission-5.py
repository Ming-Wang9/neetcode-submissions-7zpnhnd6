class MinStack:

    def __init__(self):
        self.arr = []
        self.minarr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.minarr and val<=self.minarr[-1]:
            self.minarr.append(val)
        elif self.minarr and val > self.minarr[-1]:
            self.minarr.append(self.minarr[-1])
        else:
            self.minarr.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.minarr.pop()

    def top(self) -> int:
        if self.arr:
            return self.arr[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.minarr:
            return self.minarr[-1]
        else:
            return None
        
