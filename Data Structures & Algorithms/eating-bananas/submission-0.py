class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        res=right
        while left<=right:
            mid=(left+right)//2
            t=0
            for pile in piles:
                t+=(pile+mid-1)//mid
            if t<=h:
                res=mid
                right=mid-1
            if t>h:
                left=mid+1
        return res