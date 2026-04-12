class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        total = len(nums1)+len(nums2)
        half = total // 2

        l, r = 0, len(nums1)-1
        while True:
            num1_m = l +(r-l)//2
            num2_m = half - num1_m -2

            num1_left = nums1[num1_m] if num1_m >= 0 else float("-inf")
            num1_right = nums1[num1_m +1] if (num1_m+1) < len(nums1) else float("inf")
            num2_left = nums2[num2_m] if num2_m >= 0 else float("-inf")
            num2_right = nums2[num2_m+1] if (num2_m+1) < len(nums2) else float("inf")

            if num1_left <= num2_right and num2_left <= num1_right:
                if total % 2 ==1:
                    return min(num1_right, num2_right)
                else:
                    return (max(num1_left, num2_left) +min(num1_right, num2_right)) / 2

            elif num1_left > num2_right:
                r = num1_m -1
            else:
                l = num1_m +1


