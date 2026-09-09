class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s=[]
        res=0
        for num in prices:
            while s and s[-1]>num:
                s.pop()
            
            s.append(num)
            res=max(res,num-s[0])
        return res