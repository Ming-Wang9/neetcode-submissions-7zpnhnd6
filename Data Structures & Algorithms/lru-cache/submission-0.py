class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.stack = []

    def get(self, key: int) -> int:
        for i,(k,v) in enumerate(self.stack):
            if key == k:
                self.stack.pop(i)
                self.stack.append([k,v])
                return v
        return -1
        

    def put(self, key: int, value: int) -> None:
        for i, (k,v) in enumerate(self.stack):
            if k == key:
                self.stack.pop(i)
                 
        self.stack.append([key,value])

        if len(self.stack) > self.size:
            self.stack.pop(0)




        