class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        for i in range(n-1):
            prefix[i+1]=prefix[i]*nums[i]
        for j in range(n-2,-1,-1):
            suffix[j]=suffix[j+1]*nums[j+1]
        res=[1]*n
        for m in range(n):
            res[m]=prefix[m]*suffix[m]
        return res