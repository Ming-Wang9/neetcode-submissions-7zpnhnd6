class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sub_max = []
        single_max = nums[0]
        for i in range(len(nums) - k +1):
            single_max = nums[i]
            for j in range(i, i+k):
                single_max = max(single_max, nums[j])
            sub_max.append(single_max)
        return sub_max

                