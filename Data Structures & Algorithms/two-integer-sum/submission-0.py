class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        n=len(nums)
        for i in range(n):
            if target-nums[i] not in hashmap:
                hashmap[nums[i]]=i
            else:
                return [hashmap[target-nums[i]],i]