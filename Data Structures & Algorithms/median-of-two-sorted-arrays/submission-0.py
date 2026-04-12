class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for n in nums2:
            nums1.append(n)
        nums1.sort()
        if len(nums1) %2 ==0:
            mid_pre = int(len(nums1)/2 -1)
            mid_pro = int(len(nums1) /2)
            return (nums1[mid_pre] + nums1[mid_pro])/2
        if len(nums1) %2 ==1:
            index = int(len(nums1)/2)
            return nums1[index]