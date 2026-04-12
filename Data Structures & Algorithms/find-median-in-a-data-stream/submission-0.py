class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        indx = 0
        if len(self.nums) == 1:
            return self.nums[0]
        if len(self.nums) == 2:
            return (self.nums[0] + self.nums[1]) /2
        if len(self.nums)-1%2==0:
            indx = len(self.nums)-1 // 2
            return self.nums[indx]
        if len(self.nums)-1%2!=0:
            l, r =0, len(self.nums) -1
            while True:
                l += 1
                r -= 1
                if l >r:
                    l = l -1
                    r = r+1
                    break
            return (self.nums[l]+self.nums[r]) / 2      