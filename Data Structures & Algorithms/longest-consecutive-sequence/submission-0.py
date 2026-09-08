class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        num=set(nums)
        res=0
        for i in range(n):
            if nums[i]-1 not in num:
                count=1
                current=nums[i]
                while current+1 in num:
                    count+=1
                    current+=1
                res=max(res,count)
        return res