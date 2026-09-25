class MinStack:

    def __init__(self):
        self.arr = []
        self.minarr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.minarr and self.minarr[-1]<=val:
            self.minarr.append(self.minarr[-1])
        elif self.minarr and self.minarr[-1]>val:
            self.minarr.append(val)
        else:
            self.minarr.append(val)
        
    def pop(self) -> None:
        self.arr.pop()
        self.minarr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minarr[-1]
        
