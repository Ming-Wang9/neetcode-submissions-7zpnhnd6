class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre,pro=[1]*n, [1]*n
        for i in range(1,n):
            pre[i]=pre[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            pro[j]=pro[j+1]*nums[j+1]
        res=[]
        for i in range(n):
            res.append(pre[i]*pro[i])
        return res
